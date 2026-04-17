import pytest


@pytest.mark.regression
def test_input_validation(temp_db):
    # базовая проверка на входные данные
    db, _ = temp_db
    db.create_db()

    # Проверяем отрицательные total_products
    with pytest.raises(ValueError):
        db.add_selection(-1)

    sel_id = db.add_selection(1)

    # Проверяем пустое имя товара
    with pytest.raises(ValueError):
        db.add_product(sel_id, "", 100)

    # Проверяем отрицательную цену
    with pytest.raises(ValueError):
        db.add_product(sel_id, "Продукт", -50)

    # Проверяем удаление несуществующего отбора
    deleted = db.delete_selection(999)
    assert deleted is False

    # Проверяем удаление несуществующего продукта
    deleted_prod = db.delete_product(sel_id, 999)
    assert deleted_prod is False
