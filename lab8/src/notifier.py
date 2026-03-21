# -------------------------------
# Подсистема: уведомления (Notifier)
# -------------------------------


class Notifier:
    """Отправляет уведомления клиенту (в примере — просто печатает)."""
    def notify_success(self, email: str, order_id: str) -> None:
        print(f"[NOTIFY] Уведомление: заказ {order_id} подтверждён, письмо -> {email}")

    def notify_failure(self, email: str, reason: str) -> None:
        print(f"[NOTIFY] Уведомление: заказ отменён, причина: {reason}, письмо -> {email}")
