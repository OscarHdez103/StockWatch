import sqlite3
import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path

names =["Peter Parker","Rebecca Miller"]
usernames = ["pparker","rmiller"]



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
    st.write("Success")

    #Logout
    authenticator.logout("Logout","sidebar")
    #st.sidebar.title(f"Welcome {name}")
























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
