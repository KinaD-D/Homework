import os
import sqlite3
from datetime import datetime
from typing import Any, Dict, List, Optional


class ProductDB:
    """
    Класс для работы с базой данных товаров.

    Основная идея:
    - Есть таблица "selections" (отборы)
    - Есть таблица "products" (товары), связанные с отбором через selection_id
    - Запихиваем в них отборы полученные в ходе скрейпинга
    Важно:
    - При инициализации определяется последний (максимальный) id отбора
    - Баз данных может быть несколько, но прямой защиты от одновременной работы нескольких объектов нет
    """

    DB_NAME = "products.db"

    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or self.DB_NAME
        # Получаем текущий максимальный id отбора (или 0, если БД нет)
        self.current_selection_id = self._initialize_selection_id()

    def _connect(self) -> sqlite3.Connection:
        """Создаёт и возвращает соединение с БД"""
        conn = sqlite3.connect(self.db_name)

        # Включаем поддержку внешних ключей (по умолчанию в SQLite она выключена)
        # Это нужно, чтобы работал ON DELETE CASCADE
        conn.execute("PRAGMA foreign_keys = ON")

        return conn

    def _initialize_selection_id(self) -> int:
        """
        Определяет максимальный id отбора в базе.

        1. Если файла БД нет, то возвращаем 0
        2. Если таблицы нет, то возвращаем 0
        3. Иначе берём MAX(id) из таблицы selections
        """

        if not os.path.exists(self.db_name):
            return 0

        conn = self._connect()
        try:
            cursor = conn.cursor()

            # Проверяем, существует ли таблица selections
            # sqlite_master — системная таблица SQLite с описанием структуры БД
            cursor.execute("""
                SELECT name
                FROM sqlite_master
                WHERE type='table' AND name='selections'
            """)

            if cursor.fetchone() is None:
                return 0

            # Берём максимальный id (последний созданный отбор)
            cursor.execute("SELECT MAX(id) FROM selections")
            result = cursor.fetchone()[0]

            # Если таблица пустая → result = None
            return result if result is not None else 0

        except sqlite3.Error:
            # Если что-то пошло не так, не знаю что
            return 0

        finally:
            conn.close()

    def create_db(self) -> None:
        """Создаёт таблицы базы данных, если они ещё не существуют"""

        conn = self._connect()
        try:
            cursor = conn.cursor()

            # Таблица "selections" — хранит информацию об отборе
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS selections (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- уникальный id отбора
                    date TEXT NOT NULL,                    -- дата отбора (строкой)
                    total_products INTEGER NOT NULL        -- количество товаров
                )
            """)

            # Таблица "products" — товары, привязанные к отбору
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,   -- id товара
                    selection_id INTEGER NOT NULL,          -- ссылка на отбор
                    name TEXT NOT NULL,                     -- название товара
                    price REAL NOT NULL,                    -- цена

                    -- Внешний ключ:
                    -- связывает product.selection_id с selections.id
                    -- ON DELETE CASCADE означает:
                    -- если удалить отбор, все его товары удалятся автоматически
                    FOREIGN KEY (selection_id)
                        REFERENCES selections(id)
                        ON DELETE CASCADE
                )
            """)
        except Exception as e:
            print(e)

        finally:
            conn.close()
        # Обновляем текущий id
        self._initialize_selection_id()

    def delete_db(self) -> bool:
        """Удаляет файл бд"""
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
            self.current_selection_id = 0
            return True
        return False

    def add_selection(self, total_products: int, date_value: Optional[str] = None) -> int:
        """
        Добавляет новый отбор, чтобы с ним дальше работать
        """

        if total_products < 0:
            raise ValueError("total_products не может быть отрицательным")

        date_value = date_value or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        selection_id = 0

        conn = self._connect()
        try:
            cursor = conn.cursor()

            # Вставка новой строки в таблицу selections
            # ? — это placeholder (вот это словечки понапридумывали, то есть, это защита от SQL-инъекций)
            cursor.execute(
                "INSERT INTO selections (date, total_products) VALUES (?, ?)",
                (date_value, total_products)
            )

            # lastrowid — id только что вставленной записи
            selection_id = cursor.lastrowid
            conn.commit()

        except Exception as e:
            print(e)

        finally:
            conn.close()

        self.current_selection_id = selection_id
        return selection_id

    def add_product(self, selection_id: int, name: str, price: float) -> int:
        """
        Добавляет товар в конкретный отбор.

        1. Проверяем, что отбор существует
        2. Вставляем товар
        """

        if not name:
            raise ValueError("name не может быть пустым")
        if price < 0:
            raise ValueError("price не может быть отрицательной")

        conn = self._connect()
        try:
            cursor = conn.cursor()

            # Проверяем существование отбора
            cursor.execute(
                "SELECT id FROM selections WHERE id = ?",
                (selection_id,)
            )

            if cursor.fetchone() is None:
                raise ValueError(f"Отбор с id={selection_id} не найден")

            # Вставляем товар
            cursor.execute(
                "INSERT INTO products (selection_id, name, price) VALUES (?, ?, ?)",
                (selection_id, name, price)
            )
            lastrowid = cursor.lastrowid
            conn.commit()
            return lastrowid

        except Exception as e:
            print(e)

        finally:
            conn.close()

    def delete_selection(self, selection_id: int) -> bool:
        """
        Удаляет отбор по id.
        Благодаря ON DELETE CASCADE автоматически удаляются все товары этого отбора
        """

        conn = self._connect()
        deleted = 0
        try:
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM selections WHERE id = ?",
                (selection_id,)
            )

            # rowcount > 0, запись действительно была удалена
            deleted = cursor.rowcount > 0
            conn.commit()

        except Exception as e:
            print(e)

        finally:
            conn.close()

        self._initialize_selection_id()
        return deleted

    def delete_product(self, selection_id: int, product_id: int) -> bool:
        """
        Удаляет продукт по id.
        """

        conn = self._connect()
        deleted = 0
        try:
            cursor = conn.cursor()

            cursor.execute(
                """DELETE FROM products WHERE selection_id = ? AND id = ?""",
                (selection_id, product_id)
            )

            # rowcount > 0, запись действительно была удалена
            deleted = cursor.rowcount > 0
            conn.commit()

        except Exception as e:
            print(e)

        finally:
            conn.close()

        self._initialize_selection_id()
        return deleted

    def get_all_data(self) -> List[Dict[str, Any]]:
        """
        Получает все данные из БД.

        SQL:
        1. SELECT ... FROM selections — берём отборы
        2. SELECT ... FROM products — берём товары
        3. В Python связываем их в структуру
        """

        if not os.path.exists(self.db_name):
            return []

        conn = self._connect()
        selections, products = [], []
        try:
            cursor = conn.cursor()

            # Получаем все отборы
            cursor.execute("""
                SELECT id, date, total_products
                FROM selections
                ORDER BY id
            """)
            selections = cursor.fetchall()

            # Получаем все товары
            cursor.execute("""
                SELECT id, selection_id, name, price
                FROM products
                ORDER BY id
            """)
            products = cursor.fetchall()

        except Exception as e:
            print(e)

        finally:
            conn.close()

        result: List[Dict[str, Any]] = []
        products_by_selection: Dict[int, List[Dict[str, Any]]] = {}

        # Группируем товары по selection_id
        for product_id, selection_id, name, price in products:
            products_by_selection.setdefault(selection_id, []).append({
                "product_id": product_id,
                "name": name,
                "price": price
            })

        # Собираем итоговую структуру
        for selection_id, date_value, total_products in selections:
            result.append({
                "selection_id": selection_id,
                "date": date_value,
                "total_products": total_products,
                "products": products_by_selection.get(selection_id, [])
            })

        return result

    def get_selection_info(self, selection_id: int) -> Optional[Dict[str, Any]]:
        """
        Возвращает информацию по одному отбору.
        - берём все данные
        - ищем нужный selection_id
        """

        all_data = self.get_all_data()

        for item in all_data:
            if item["selection_id"] == selection_id:
                return item

        return None
