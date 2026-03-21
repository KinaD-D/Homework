from typing import Optional
from inventory import Inventory
from notifier import Notifier
from payment import Payment
from shipping import Shipping


# -------------------------------
# Фасад: OrderProcessor
# -------------------------------
class OrderProcessor:
    """
    Фасад, который предоставляет единый метод для оформления заказа:
    place_order(customer_email, address, sku, qty, card_number, price_per_unit)
    Фасад скрывает сложную последовательность операций и выполняет откат при ошибках.
    """
    _order_counter = 0

    def __init__(self, inventory: Inventory, payment: Payment, shipping: Shipping, notifier: Notifier) -> None:
        self._inventory = inventory
        self._payment = payment
        self._shipping = shipping
        self._notifier = notifier

    def _new_order_id(self) -> str:
        OrderProcessor._order_counter += 1
        return f"order{OrderProcessor._order_counter}"

    def place_order(self, email: str, address: str, sku: str, qty: int, card_number: str, price_per_unit: float) -> Optional[str]:
        # Основной метод фасада: оформляет заказ и возвращает order_id при успехе.
        # При неудаче — возвращает None (и выполняет компенсации).
        order_id = self._new_order_id()
        total = price_per_unit * qty

        # 1) Резервируем товар
        reserved = self._inventory.reserve(sku, qty)
        if not reserved:
            # если не получилось зарезервировать, уведомляем и завершаем
            self._notifier.notify_failure(email, "Товар отсутствует на складе")
            return None

        tx_id = None

        try:
            # 2) Снимаем платёж
            tx_id = self._payment.charge(card_number, total)

            # 3) Создаём отправление
            ship_id = self._shipping.create_shipment(address, sku, qty)

            # 4) Уведомляем клиента об успешном оформлении
            self._notifier.notify_success(email, order_id)

            # печатаем диагностическую информацию
            print(f"[ORDER] Успешно: order={order_id}, tx={tx_id}, ship={ship_id}, sku={sku}, qty={qty}, total={total:.2f}")
            return order_id

        except Exception as exc:
            # если что-то пошло не так — выполняем rollback
            reason = str(exc)
            print(f"[ORDER] Ошибка при оформлении заказа {order_id}: {reason}")

            # если платёж прошёл, пробуем сделать refund
            if tx_id:
                try:
                    refunded = self._payment.refund(tx_id, total)
                    print(f"[REFUND] Транзакция {tx_id} возмещена: {refunded}")
                except Exception as rexc:
                    print(f"[REFUND] Ошибка при возврате {tx_id}: {rexc}")

            # освобождаем резерв на складе
            self._inventory.release(sku, qty)
            # уведомляем клиента об ошибке
            self._notifier.notify_failure(email, reason)
            return None
