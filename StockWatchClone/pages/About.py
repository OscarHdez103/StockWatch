import streamlit as st
st.markdown("<h1 style='text-align: center;'>About 🧠</h1>", unsafe_allow_html=True)

def about():
    st.subheader("Test123")
    # with open("PresentationStockWatch.pdf", "rb") as f: pdf_bytes = f.read() pdf_base64 = b64encode(
    # pdf_bytes).decode('utf-8') pdf_embed = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700"
    # height="300" type="application/pdf"></iframe>'
    #
    # st.markdown(pdf_embed, unsafe_allow_html=True)


def main():
    st.title("StockWatch")
    about()


if __name__ == '__main__':
    about()