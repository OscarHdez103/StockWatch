from base64 import b64encode

import streamlit as st
# st.sidebar.image("StockWatchLogo.png")
#
# st.markdown("<h1 style='text-align: center;'>About</h1>", unsafe_allow_html=True)
# #st.markdown("<h1 style='text-align: center;'>Using StockWatch</h1>", unsafe_allow_html=True)
# st.markdown('<div style="text-align: center;">StockWatch is a comprehensive dashboard that enables you to effortlessly track national-level and individual supermarket stock for various products.</div>',unsafe_allow_html=True)
#

with open('stockwatch.pdf', "rb") as f:
    pdf_bytes = f.read()
    pdf_base64 = b64encode(pdf_bytes).decode('utf-8')
    pdf_embed = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="300" ' \
                f' type="application/pdf"></iframe>'
st.subheader("Brishack 2023 - Team StockWatch")

st.markdown(pdf_embed, unsafe_allow_html=True)
# def about():
#     with open('stockwatch.pdf', "rb") as f:
#         pdf_bytes = f.read()
#         pdf_base64 = b64encode(pdf_bytes).decode('utf-8')
#         pdf_embed = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="300" ' \
#                     f' type="application/pdf"></iframe>'
#     st.subheader("Brishack 2023 - Team StockWatch")
#
#     st.markdown(pdf_embed, unsafe_allow_html=True)
#
#
# def main():
#     st.title("StockWatch")
#     about()
#
#
# if __name__ == '__main__':
#     about()
