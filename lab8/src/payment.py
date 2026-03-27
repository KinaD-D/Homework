# -------------------------------
# Подсистема: платёжный шлюз (Payment)
# -------------------------------


class Payment:
    """
    Упрощённый платёжный шлюз.
    Но по-приколу тут всё равно есть лишние переменные.
    Метод charge поднимает исключение при отклонении платежа.
    """
    _tx_counter = 0  # примитивный счётчик транзакций

    @staticmethod
    def charge(card_number: str, amount: float) -> str:
        # Пытаемся снять сумму. В этом примере платеж будет отклонён,
        # если номер карты заканчивается на '0000' (симулируем отказ).
        if card_number.endswith("0000"):
            raise RuntimeError("Платёж отклонён эмитентом карты")
        Payment._tx_counter += 1
        tx_id = f"tx{Payment._tx_counter}"
        return tx_id

    @staticmethod
    def refund(tx_id: str, amount: float) -> bool:
        # Компенсация платежа (в нашем случае всегда успешна)
        return True
