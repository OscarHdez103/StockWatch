import sqlite3

conn = sqlite3.connect('data/Supermarkets.db')
c = conn.cursor()


def total(product, supermarket):
    c.execute("SELECT product_quantity FROM '" + supermarket + "' WHERE product_name = '" + product + "'")
    quantity = c.fetchall()
    c.execute("UPDATE Products SET quantity_total = quantity_total +  ? WHERE product_name = ?", (quantity[0][0], product.title()))
    conn.commit()


def all_products():
    c.execute("UPDATE Products SET quantity_total = 0")
    c.execute("SELECT product_name FROM Products")
    products = c.fetchall()
    c.execute("SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%' AND name NOT LIKE 'Products';")
    supermarkets = c.fetchall()
    for supermarket in supermarkets:
        for product in products:
            total(product[0], supermarket[0])


def main():
    all_products()
    conn.close()


if __name__ == '__main__':
    main()
    conn.close()

