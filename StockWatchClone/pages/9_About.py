from base64 import b64encode

import streamlit as st

st.sidebar.image("StockWatchLogo.png")

st.markdown("<h1 style='text-align: center;'>About</h1>", unsafe_allow_html=True)

st.markdown('<div style="text-align: center;">StockWatch is a comprehensive dashboard that enables you to '
            'effortlessly track national-level and individual supermarket stock for various products.</div>',
            unsafe_allow_html=True)

f = open(r'pages\stockwatch.pdf', "rb")
pdf_bytes = f.read()
pdf_base64 = b64encode(pdf_bytes).decode('utf-8')
pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" width="100%" height=500 ' \
            f' type="application/pdf">'
st.subheader("BrisHack 2023 - StockWatch")

st.markdown(pdf_embed, unsafe_allow_html=True)
