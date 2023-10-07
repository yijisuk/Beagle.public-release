import streamlit as st
from streamlit_pages.mainpage import MainPage

if __name__ == "__main__":

    st.set_page_config(layout="wide")
    mainpage = MainPage()