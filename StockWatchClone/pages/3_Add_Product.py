import sqlite3
import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path

conn = sqlite3.connect('data/Supermarkets.db')
c = conn.cursor()

names =["Peter Parker","Rebecca Miller"]
usernames = ["pparker","rmiller"]

def verifyProduct(new_product,new_cost):
    c.execute("SELECT product_name FROM Products")
    co = c.fetchall()
    #st.write(co)
    query_result = product_search("Products",new_product)
    if len(query_result) < 1:
        if new_cost != "":
            if new_product != "":
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
def add_product(product,category,cost,quantity):
    c.execute("SELECT product_name FROM Products")
    co = c.fetchall()
    ids = len(co)
    c.execute("INSERT INTO Products VALUES (?,?,?,?)",(ids,product,category,0))

    supermarkets = ["Tesco", "Iceland", "Asda", "Morrisons", "Co-op"]
    for shop in supermarkets:
        c.execute("SELECT product_supplier FROM '"+shop+"'")
        sup = c.fetchall()
        sup1 = sup[0][0]

        c.execute("INSERT INTO '"+shop+"' VALUES (?,?,?,?,?,?,?)",(ids,product,category,"100g",cost,quantity,sup1))
    conn.commit()

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











file_path = Path(__file__).parent / "user_data/hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

credentials = {"usernames": {}}

for uname, name, pwd in zip(usernames, names, hashed_passwords):
    user_dict = {"name": name, "password": pwd}
    credentials["usernames"].update({uname: user_dict})

authenticator = stauth.Authenticate(credentials,"addition_dashboard","abc", cookie_expiry_days=30)
name,authentication_status,username = authenticator.login("Login","main")

if authentication_status == False:
    st.error("Username/Password is incorrect")
if authentication_status == None:
    st.warning("Please enter your username and password")
if authentication_status:
    #st.write("Success")

    #Logout
    authenticator.logout("Logout","sidebar")
    #st.sidebar.title(f"Welcome {name}")
    st.markdown("<h1 style='text-align: center;'>Add Product Data</h1>", unsafe_allow_html=True)
    catagories =["Beverage","Fresh","Dry Foods","Snacks"]
    cols = st.columns(4)
    with cols[0]:
        new_product = st.text_input("Input Product Name")
    with cols[1]:
        new_catagory = st.selectbox("Catagory",catagories)
    with cols[2]:
        new_cost = st.text_input("Cost")
    with cols[3]:
        new_quantity = st.text_input("Input Stock")
    submit = st.button("Add")
    if submit:
        if verifyProduct(new_product,new_cost) == True:
            add_product(new_product,new_catagory,new_cost,new_quantity)
            all_products()
            st.success("Success!")

        elif verifyProduct(new_product,new_cost) == False:
            st.error("Failure - Ensure all fields are populated and the product is unique")


# def verifyProduct(new_product,new_cost):
#     c.execute("SELECT product_name FROM Products")
#     co = c.fetchall().toList()
#     st.write(co)
#     if new_cost != Null:
#         if new_product != NULL:
#             if co.count(new_product.title()) < 1:
#                 return True
#     return False
conn.close()






















# usernames = ['user1', 'user2']
# names = ['name1', 'name2']
# passwords = ['pwd1', 'pwd2']
#
# credentials = {"usernames": {}}
#
# for uname, name, pwd in zip(usernames, names, passwords):
#     user_dict = {"name": name, "password": pwd}
#     credentials["usernames"].update({uname: user_dict})
#
#
# #st.markdown("<h1 style='text-align: center;'>Add Product</h1>", unsafe_allow_html=True)
#
#
#
#
#
#
# def main(credentials):
#     authenticator = stauth.Authenticate(credentials, "cookie_name", "random_key", cookie_expiry_days=30)
#
#     authentication_status = authenticator.login('Login', 'main')
#
#     if authentication_status:
#         st.subheader("Welcome")
#         # your application
#     elif authentication_status == False:
#         st.error("Username / password is incorrect")
#     elif authentication_status == None:
#         st.warning("Please enter your username and password")
#
#
# if __name__ == '__main__':
#     main(credentials)
