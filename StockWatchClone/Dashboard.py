import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('data/Supermarkets.db')
c = conn.cursor()



def tabulate(supermarket, data):
    query_df = pd.DataFrame(product_search(supermarket, data))
    if supermarket == "Products":
        query_df.columns = ["Name", "Category", "Total"]
    else:
        query_df.columns = ["Name", "Category", "Description", "Cost", "Quantity"]
    st.dataframe(query_df)


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
            data[i] = data[i][1:end-1]
    return data


def home():
    st.markdown("<h1 style='text-align: center;'>StockWatch</h1>", unsafe_allow_html=True)
    supermarkets = ["Products", "Tesco", "Iceland", "Asda", "Morrisons", "Co-op"]
    col1, col2 = st.columns(2)
    with col1:
        supermarkets_selector = st.selectbox("Supermarket", supermarkets)
        with st.form(key='query_form'):
            product = st.text_input("Search product")
            submit_code = st.form_submit_button("Search")

    with col2:
        if submit_code:
            tabulate(supermarkets_selector, product)
        else:
            tabulate(supermarkets_selector, "")


if __name__ == '__main__':
    home()
