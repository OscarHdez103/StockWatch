import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
c = conn.cursor()


def sql_executor(raw_code):
    c.execute(raw_code)
    data = c.fetchall()
    return data


def main():
    st.title("Lux")
    menu = ["Home", "Login", "Create Account", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("HomePage")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("Look up here")
                submit_code = st.form_submit_button("Execute")
            with st.expander("Table Info"):
                t_info = {}

        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)
                query_results = sql_executor(raw_code)
                with st.expander("Results"):
                    st.write(query_results)
                with st.expander("Pretty Table"):
                    query_df = pd.DataFrame(query_results)
                    st.dataframe(query_df)

    elif choice == "About":
        st.subheader("About")
    elif choice == "Create Account":
        st.subheader("Create Account")
    elif choice == "Login":
        st.subheader("Login")


if __name__ == '__main__':
    main()
