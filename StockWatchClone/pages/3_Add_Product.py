import sqlite3
import streamlit as st
import streamlit_authenticator as stauth


def login():
    #st.markdown("<h1 style='text-align: center;'>Add Product</h1>", unsafe_allow_html=True)
    names = ['John Smith', 'Rebecca Briggs']
    usernames = ['jsmith', 'rbriggs']
    passwords = ['123', '456']
    hashed_passwords = stauth.hasher(passwords).generate()
    authenticator = stauth.authenticate(names, usernames, hashed_passwords, 'cookie_name', '1234', cookie_expiry_days=30)
    name, authentication_status = authenticator.login('Login', 'sidebar')
    if authentication_status:
        st.write("Welcome * % s *" % (name))
        # your application
    elif authentication_status == False:
        st.error("Username / password is incorrect")
    elif authentication_status == None:
        st.warning("Please enter your username and password")







if __name__ == '__main__':
    login()
