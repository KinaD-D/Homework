import os
import tempfile
import pytest

from database.product_database import ProductDB


@pytest.fixture
def temp_db():
    with tempfile.TemporaryDirectory() as tmp_dir:
        try:
            db_path = os.path.join(tmp_dir, "test_products.db")
            db = ProductDB(db_path)
            yield db, db_path
        except Exception as e:
            raise RuntimeError("DB is not available")


