import sqlite3


def connection():
    conn = sqlite3.connect('data/Supermarkets.db')
    c = conn.cursor()
    return conn, c


def product_search(supermarket, product):
    conn, c = connection()
    if product == "":
        c.execute("SELECT * FROM '" + supermarket + "'")
    else:
        c.execute("SELECT * FROM '" + supermarket + "' WHERE product_name = ?", (product.title(),))
    data = c.fetchall()
    conn.close()
    return data


def get_supermarkets():
    conn, c = connection()
    c.execute(
        "SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%' AND name NOT LIKE 'Products';")
    supermarkets = c.fetchall()
    conn.close()
    return supermarkets


def total(product, supermarket, cursor):
    cursor.execute("SELECT product_quantity FROM '" + supermarket + "' WHERE product_name = '" + product + "'")
    quantity = cursor.fetchall()
    cursor.execute("UPDATE Products SET quantity_total = quantity_total +  ? WHERE product_name = ?",
                   (quantity[0][0], product.title()))


def all_products():
    conn, c = connection()
    c.execute("UPDATE Products SET quantity_total = 0")
    c.execute("SELECT product_name FROM Products")
    products = c.fetchall()
    supermarkets = get_supermarkets()
    for supermarket in supermarkets:
        for product in products:
            total(product[0], supermarket[0], c)
    conn.commit()
    conn.close()


def main():
    all_products()


if __name__ == '__main__':
    main()
