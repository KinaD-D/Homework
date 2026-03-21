from typing import Dict

# -------------------------------
# Подсистема: учёт запасов (Inventory)
# Nichego interesnogo
# -------------------------------


class Inventory:
    """
    Простая подсистема управления запасами.
    Хранит количество на складе и умеет резервировать / освобождать товар.
    """
    def __init__(self, initial_stock: Dict[str, int]) -> None:
        # словарь: sku -> количество
        self._stock = dict(initial_stock)

    def check(self, sku: str, qty: int) -> bool:
        # Проверить, что на складе достаточно товара.
        return self._stock.get(sku, 0) >= qty

    def reserve(self, sku: str, qty: int) -> bool:
        # Попытаться зарезервировать qty единиц товара.
        # Возвращает True при успехе, False если недостаточно.

        if self.check(sku, qty):
            self._stock[sku] = self._stock.get(sku, 0) - qty
            return True
        return False

    def release(self, sku: str, qty: int) -> None:
        # ранее зарезервированные единицы (компенсация).
        self._stock[sku] = self._stock.get(sku, 0) + qty

    def stock(self, sku: str) -> int:
        # Текущее количество на складе (для диагностики)
        return self._stock.get(sku, 0)
