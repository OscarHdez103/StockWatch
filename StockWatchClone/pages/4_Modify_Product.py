import streamlit as st

import sqlite3

conn = sqlite3.connect('data/Supermarkets.db')
c = conn.cursor()


def total(product, supermarket):
    c.execute("SELECT product_quantity FROM " + supermarket + " WHERE product_name = '" + product + "'")
    quantity = c.fetchall()
    c.execute("UPDATE Products SET quantity_total = quantity_total +  ? WHERE product_name = ?",
              (quantity[0][0], product.title()))
    conn.commit()


def all_products():
    c.execute("UPDATE Products SET quantity_total = 0")
    c.execute("SELECT product_name FROM Products")
    names = c.fetchall()
    for name in names:
        for supermarket in ["Tesco", "Iceland", "Asda", "Morrisons", "`Co-op`"]:
            total(name[0], supermarket)


def set_product(supermarket, data, quantity):
    if data == "":
        st.write("")
        return

    if not is_product(supermarket, data):
        st.error("Product not found")
        return

    query = "UPDATE {} SET product_quantity = ? WHERE product_name = ?".format(supermarket)
    c.execute(query, (quantity, data))
    conn.commit()

    all_products()

    st.write("Product quantity updated!")


def add_to_product(supermarket, data, quantity):
    if data == "":
        st.write("")
        return

    if not is_product(supermarket, data):
        st.error("Product not found")
        return

    query = "UPDATE {} SET product_quantity = product_quantity + ? WHERE product_name = ?".format(supermarket)
    c.execute(query, (quantity, data))
    conn.commit()

    all_products()

    st.write("Product quantity updated!")


def is_product(supermarket, data):
    query_result = product_search(supermarket, data)
    if len(query_result) > 0:
        return True
    return False


def product_search(supermarket, product):
    if product == "":
        c.execute("SELECT * FROM '" + supermarket + "'")
    else:
        c.execute("SELECT * FROM '" + supermarket + "' WHERE product_name = '" + product.title() + "'")
    data = c.fetchall()
    for i in range(len(data)):
        end = len(data[i])
        if len(data[i]) == 4:
            data[i] = data[i][1:end]
        else:
            data[i] = data[i][1:end - 1]
    return data


def home():
    st.markdown("<h1 style='text-align: center;'>StockWatch</h1>", unsafe_allow_html=True)
    # st.sidebar.image("StockWatchLogo.png", use_column_width=True)
    supermarkets = ["Tesco", "Iceland", "Asda", "Morrisons", "Co-op"]
    col1, col2 = st.columns(2)
    with col1:
        supermarkets_selector = st.selectbox("Supermarket", supermarkets)
        with st.form(key='query_form'):
            product = st.text_input("Search product")
            quantity = st.text_input("New quantity")
            colm1, colm2 = st.columns(2)
            with colm1:
                submit_code = st.form_submit_button("Update quantity")
            with colm2:
                submit_code_add = st.form_submit_button("Add quantity to")

    with col2:
        if submit_code:
            set_product(supermarkets_selector, product.title(), quantity)
        elif submit_code_add:
            add_to_product(supermarkets_selector, product.title(), quantity)


if __name__ == '__main__':
    home()
