from database.product_database import ProductDB


def main():
    db = ProductDB()
    db.create_db()

    selection_id = db.add_selection(total_products=2)
    db.add_product(selection_id, "Ноутбук", 75000)
    db.add_product(selection_id, "Мышка", 1500)

    data = db.get_all_data()
    for item in data:
        print(f"Отбор №{item['selection_id']}, дата: {item['date']}, товаров: {item['total_products']}")
        for product in item["products"]:
            print(f"  - {product['name']} — {product['price']} руб.")

    print("\nТекущий порядковый номер:", db.current_selection_id)


if __name__ == "__main__":
    main()
