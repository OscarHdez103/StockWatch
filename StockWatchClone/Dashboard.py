from copy import copy
import Backend
import streamlit as st
import altair as alt
import pandas as pd
import sqlite3

# st.sidebar.image("StockWatchLogo.png")


def display_products(supermarket, product):
    data = Backend.product_search(supermarket, product)
    for i in range(len(data)):
        end = len(data[i])
        if len(data[i]) == 4:
            data[i] = data[i][1:end]
        else:
            data[i] = data[i][1:end - 1]
    return data


def add_graph(super, data, color):
    supermarkets = copy(super)

    if data == "":
        st.write("")
        return
    if not is_product(supermarkets, data):
        st.error("Product not found")
        return
    supermarkets.remove("Products")
    quantities = []
    for supermarket in supermarkets:
        query_df = pd.DataFrame(display_products(supermarket, data))
        if supermarket == "Products":
            quantities.append(query_df[2].tolist())
        else:
            quantities.append(query_df[4].tolist())

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
        width=250,
    )

    st.altair_chart(chart)


def is_product(supermarkets, data):
    for supermarket in supermarkets:
        query_result = Backend.product_search(supermarket, data)
        if len(query_result) > 0:
            return True
    return False


def tabulate(supermarket, data):
    query_df = pd.DataFrame(display_products(supermarket, data))
    if supermarket == "Products":
        query_df.columns = ["Name", "Category", "Total"]
    else:
        query_df.columns = ["Name", "Category", "Description", "Cost", "Quantity"]
    st.dataframe(query_df)





def home():
    st.markdown("<h1 style='text-align: center;'>StockWatch</h1>", unsafe_allow_html=True)
    # st.sidebar.image("StockWatchLogo.png", use_column_width=True)
    supermarkets = ["Products", "Tesco", "Iceland", "Asda", "Morrisons", "Co-op"]
    col1, col2 = st.columns(2)
    with col1:
        supermarkets_selector = st.selectbox("Supermarket", supermarkets)
        with st.form(key='query_form'):
            product = st.text_input("Search product")
            submit_code = st.form_submit_button("Search")
        # color = st.color_picker('', '#55ACEE')
        color = '#55ACEE'

    with col2:
        if submit_code:
            tabulate(supermarkets_selector, product)
            if (supermarkets_selector == "Products") & submit_code:
                add_graph(supermarkets, product.title(), color)
        else:
            tabulate(supermarkets_selector, "")


if __name__ == '__main__':
    home()
