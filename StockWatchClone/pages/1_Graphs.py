import sqlite3

import altair as alt
import pandas as pd
import streamlit as st

st.markdown("<h1 style='text-align: center;'>Graphs and Data </h1>", unsafe_allow_html=True)

conn = sqlite3.connect('data/Supermarkets.db')
c = conn.cursor()
# st.sidebar.image("StockWatchLogo.png")


def add_graph(supermarkets, data, color):
    if data == "":
        st.write("")
        return
    if not is_product(supermarkets, data):
        st.error("Product not found")
        return
    supermarkets.remove("Products")
    quantities = []
    for supermarket in supermarkets:
        query_df = pd.DataFrame(product_search(supermarket, data))
        if supermarket == "Products":
            quantities.append(query_df[3].tolist())
        else:
            quantities.append(query_df[5].tolist())

    # Flatten the list of Series to a list of values
    quantities = sum(quantities, [])

    df = pd.DataFrame({'Supermarkets': supermarkets, 'Quantity': quantities})

    df['Supermarkets'] = df['Supermarkets'].astype(str)

    # Define the chart
    chart = alt.Chart(df).mark_bar().encode(
        x='Supermarkets',
        y='Quantity',
        color=alt.ColorValue(color),
    ).properties(
        width=700,
    )

    st.altair_chart(chart)


def is_product(supermarkets, data):
    for supermarket in supermarkets:
        query_result = product_search(supermarket, data)
        if len(query_result) > 0:
            return True
    return False


def product_search(supermarket, product):
    if product == "":
        c.execute("SELECT * FROM '" + supermarket + "'")
    else:
        c.execute("SELECT * FROM '" + supermarket + "' WHERE product_name = ?", (product.title(),))
    data = c.fetchall()
    return data


def graph():
    supermarkets = ["Products", "Tesco", "Iceland", "Asda", "Morrisons", "Co-op"]

    with st.form(key='query_form'):
        product = st.text_input("Search product")
        submit_code = st.form_submit_button("Search")
    cols = st.columns(22)
    with cols[1]:
        color = st.color_picker('', '#55ACEE')
    if submit_code:
        add_graph(supermarkets, product.title(), color)
    else:
        add_graph(supermarkets, "Bread", color)


if __name__ == '__main__':
    graph()
    conn.close()
