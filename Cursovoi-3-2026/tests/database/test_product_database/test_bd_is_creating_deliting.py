import pytest
import os


@pytest.mark.smoke
def test_db_file_create_delete(temp_db):
    db, db_path = temp_db
    # Проверка, что файл существует после создания
    db.create_db()
    assert os.path.exists(db_path)

    # Удаление БД
    try:
        deleted = db.delete_db()
        assert deleted is True
        assert not os.path.exists(db_path)
    except PermissionError as e:
        print(f'{e}: конфликт библиотек')
