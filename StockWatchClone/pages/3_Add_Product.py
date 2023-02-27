import sqlite3
import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path

import Backend
import Dashboard

st.sidebar.image("StockWatchLogo.png")

names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]


def verify_product(new_product, new_cost):
    query_result = Backend.product_search("Products", new_product)
    if len(query_result) < 1:
        if new_cost != "":
            if new_product != "":
                return True
    return False


def add_product(product, category, cost, quantity):
    conn, c = Backend.connection()
    c.execute("SELECT product_name FROM Products")
    co = c.fetchall()
    ids = len(co)
    c.execute("INSERT INTO Products VALUES (?,?,?,?)", (ids, product, category, 0))

    supermarkets = ["Tesco", "Iceland", "Asda", "Morrisons", "Co-op"]
    for shop in supermarkets:
        c.execute("SELECT product_supplier FROM '" + shop + "'")
        sup = c.fetchall()
        sup1 = sup[0][0]

        c.execute("INSERT INTO '" + shop + "' VALUES (?,?,?,?,?,?,?)",
                  (ids, product, category, "100g", cost, quantity, sup1))
    conn.commit()
    conn.close()


file_path = Path(__file__).parent / "user_data/hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

credentials = {"usernames": {}}

for uname, name, pwd in zip(usernames, names, hashed_passwords):
    user_dict = {"name": name, "password": pwd}
    credentials["usernames"].update({uname: user_dict})

authenticator = stauth.Authenticate(credentials, "addition_dashboard", "abc", cookie_expiry_days=30)
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/Password is incorrect")
if authentication_status == None:
    st.warning("Please enter your username and password")
if authentication_status:
    # st.write("Success")

    # Logout
    authenticator.logout("Logout", "sidebar")

    st.markdown("<h1 style='text-align: center;'>Add Product Data</h1>", unsafe_allow_html=True)
    categories = ["Beverage", "Fresh", "Dry Foods", "Snacks"]
    cols = st.columns(4)
    with cols[0]:
        new_product = st.text_input("Input Product Name")
        new_product = new_product.title()
    with cols[1]:
        new_category = st.selectbox("Category", categories)
    with cols[2]:
        new_cost = st.text_input("Cost")
    with cols[3]:
        new_quantity = st.text_input("Input Stock")
    submit = st.button("Add")
    if submit:
        if verify_product(new_product, new_cost) == True:
            add_product(new_product, new_category, new_cost, new_quantity)
            Backend.all_products()
            st.success("Success!")

        elif verify_product(new_product, new_cost) == False:
            st.error("Failure - Ensure all fields are populated and the product is unique")
