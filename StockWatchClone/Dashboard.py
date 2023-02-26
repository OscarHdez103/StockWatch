import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('data/Supermarkets.db')
c = conn.cursor()


def tabulate(supermarket, data):
    query_df = pd.DataFrame(product_search(supermarket, data))
    if supermarket == "Products":
        query_df.columns = ["Id", "Name", "Category", "Total"]
    else:
        query_df.columns = ["Id", "Name", "Category", "Description", "Cost", "Quantity", "Supplier"]
    st.dataframe(query_df)


def sql_executor(query):  # work in progress
    c.execute(query)
    data = c.fetchall()
    return data

def product_search(supermarket,product):

    if product == "":
        c.execute("SELECT * FROM '" + supermarket + "'")
    else:
        c.execute("SELECT * FROM '"+supermarket+"' WHERE product_name = '"+product+"'")
    data = c.fetchall()
    return data


def home():
    st.markdown("<h1 style='text-align: center; color: black;'>StockWatch</h1>", unsafe_allow_html=True)
    supermarkets = ["Products", "Tesco", "Iceland", "Asda", "Morrisons", "Co-op"]
    col1, col2 = st.columns(2)
    with col1:
        supermarkets_selector = st.selectbox("Supermarket", supermarkets)  # doesn't do anything yet
        with st.form(key='query_form'):
            product = st.text_area("Search product")
            submit_code = st.form_submit_button("Search")

    with col2:
        if submit_code:
            with st.expander("Pretty Table"):
                tabulate(supermarkets_selector, product)





if __name__ == '__main__':
    home()