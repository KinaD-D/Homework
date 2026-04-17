import pytest


@pytest.mark.smoke
def test_add_selection_products_delete(temp_db):
    #  Помимо проверки функций добавления и удаления, проверяются и функции возвращения информации
    db, _ = temp_db
    db.create_db()

    # Добавляем отбор
    sel_id = db.add_selection(2)
    data = db.get_all_data()
    assert len(data) == 1
    assert data[0]["selection_id"] == sel_id
    assert data[0]["total_products"] == 2
    info = db.get_selection_info(sel_id)
    assert info is not None

    # Добавляем товары
    prod1 = db.add_product(sel_id, "Ноутбук", 75000)
    prod2 = db.add_product(sel_id, "Мышка", 1500)
    info = db.get_selection_info(sel_id)
    assert len(info["products"]) == 2

    # Удаляем продукт
    deleted_prod = db.delete_product(sel_id, prod1)
    assert deleted_prod is True
    info = db.get_selection_info(sel_id)
    assert len(info["products"]) == 1

    # Удаляем весь отбор
    deleted_sel = db.delete_selection(sel_id)
    assert deleted_sel is True
    data = db.get_all_data()
    assert data == []
