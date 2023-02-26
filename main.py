import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('data/Supermarkets.db')
c = conn.cursor()


def tabulate(supermarket, data):
    query_df = pd.DataFrame(product_search(supermarket, data))
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


def about():
    st.subheader("About")
    # with open("PresentationStockWatch.pdf", "rb") as f: pdf_bytes = f.read() pdf_base64 = b64encode(
    # pdf_bytes).decode('utf-8') pdf_embed = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700"
    # height="300" type="application/pdf"></iframe>'
    #
    # st.markdown(pdf_embed, unsafe_allow_html=True)


def main():
    st.title("StockWatch")
    menu = ["Home", "About"]
    home()

    with st.sidebar:
        st.button("Home", on_click=home)
        st.button("About", on_click=about)


if __name__ == '__main__':
    main()
