# -------------------------------
# Подсистема: уведомления (Notifier)
# Здесь только они, без других версий [чего-либо]
# -------------------------------


class Notifier:
    """Отправляет уведомления клиенту (в примере — просто печатает)."""
    @staticmethod
    def notify_success(email: str, order_id: str) -> None:
        print(f"[NOTIFY] Уведомление: заказ {order_id} подтверждён, письмо -> {email}")

    @staticmethod
    def notify_failure(email: str, reason: str) -> None:
        print(f"[NOTIFY] Уведомление: заказ отменён, причина: {reason}, письмо -> {email}")
