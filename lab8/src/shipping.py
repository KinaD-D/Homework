# -------------------------------
# Подсистема: логистика / доставка (Shipping)
# -------------------------------


class Shipping:
    """
    Создаёт отправление. Возвращает идентификатор отгрузки.
    """
    _ship_counter = 0

    @staticmethod
    def create_shipment(address: str, sku: str, qty: int) -> str:
        Shipping._ship_counter += 1
        return f"ship{Shipping._ship_counter}"
