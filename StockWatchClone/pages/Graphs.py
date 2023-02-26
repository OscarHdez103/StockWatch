import sqlite3
import pandas as pd
import streamlit as st

st.markdown("<h1 style='text-align: center;'>Graphs and Data 📊</h1>", unsafe_allow_html=True)

conn = sqlite3.connect('data/Supermarkets.db')
c = conn.cursor()


def add_graph(supermarkets, data):
    if data == "":
        st.write("Input a product")
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

    df = pd.DataFrame({'labels': supermarkets, 'Quantity': quantities})

    df['labels'] = df['labels'].astype(str)

    # Set the 'labels' column as the index
    df.set_index('labels', inplace=True)

    # Create the bar chart
    st.bar_chart(df)

def is_product(supermarkets, data):
    for supermarket in supermarkets:
        query_result = product_search(supermarket, data)
        if len(query_result) > 0:
            return True
    return False
def sql_executor(query):  # work in progress
    c.execute(query)
    data = c.fetchall()
    return data


def product_search(supermarket, product):
    if product == "":
        c.execute("SELECT * FROM '" + supermarket + "'")
    else:
        c.execute("SELECT * FROM '" + supermarket + "' WHERE product_name = '" + product + "'")
    data = c.fetchall()
    return data


def graph():
    supermarkets = ["Products", "Tesco", "Iceland", "Asda", "Morrisons", "Co-op"]
    col1, col2 = st.columns(2)
    with col1:
        with st.form(key='query_form'):
            product = st.text_input("Search product")
            submit_code = st.form_submit_button("Search")

    with col2:
        if submit_code:
            add_graph(supermarkets, product)
        else:
            add_graph(supermarkets, "")


if __name__ == '__main__':
    graph()
