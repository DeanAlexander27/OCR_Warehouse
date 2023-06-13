import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title = "OCR Warehouse",
                   page_icon = ":bar_chart:",
                   layout = "wide"
                   )

# ---- TABBAR ----
tab1, tab2 = st.tabs(["Welcome Page", "This is your solution"])
tab1.title("Welcome to Application OCR Warehouse")
tab1.header("In this tool will help you to reduce manual activities of rechecking documents")
tab2.header("OCR Warehouse is a tool deep learning using CNN to use classification image")

st.sidebar.success("Select a page above")
