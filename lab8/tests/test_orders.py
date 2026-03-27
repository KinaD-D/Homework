from src.Лабараторная8 import main
from src.notifier import Notifier
import pytest


# Проверка системы на базовою работоспособность (хотя здесь специально допущены ошибки ради задания)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("inventory, text_that_need", [
    (None, "[NOTIFY]"),
    ({'ЧайОк': 10}, "[REFUND}"),
    ({'apple': 150}, "[ORDER]"),
    ({}, "[WOW]")
])
def test_for_orders(inventory, text_that_need, capsys):
    main(inventory)
    assert text_that_need in capsys.readouterr().out


@pytest.mark.regression
@pytest.mark.parametrize("func", [
    lambda: Notifier.notify_failure('', ''),
    lambda: Notifier.notify_success('', '')
])
def test_notify(func, capsys):
    func()
    assert '[NOTIFY]' in capsys.readouterr().out
