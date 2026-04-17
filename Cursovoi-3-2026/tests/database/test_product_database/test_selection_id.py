import pytest
from database.product_database import ProductDB

@pytest.mark.regression
def test_selection_id_persistence(temp_db):
    db, _ = temp_db
    db.create_db()

    # Добавляем отбор
    sel1 = db.add_selection(1)
    db.add_product(sel1, "Продукт1", 100)
    sel2 = db.add_selection(2)
    db.add_product(sel2, "Продукт2", 200)

    # Закрываем и заново создаём объект
    new_db_instance = ProductDB(db.db_name)
    # Проверяем, что current_selection_id = максимальный
    assert new_db_instance.current_selection_id == sel2


@pytest.mark.regression
@pytest.mark.xfail(reason="Одновременная работа двух объектов на одну БД может привести к конфликту ID")
def test_simultaneous_objects(temp_db):
    db1, _ = temp_db
    db1.create_db()
    db2 = ProductDB(db1.db_name)

    sel1 = db1.add_selection(1)
    sel2 = db2.add_selection(1)

    # Если оба объекта корректно обрабатывают selection_id, sel2 > sel1
    assert sel2 > sel1
