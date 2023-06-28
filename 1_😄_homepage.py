import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title = "OCR Warehouse",
                   page_icon = ":bar_chart:",
                   layout = "wide"
                   )

# ---- TABBAR ----
tab1, tab2, tab3 = st.tabs(["Welcome Page", "This is your solution", "what often goes wrong in the warehouse?"])
tab1.title("Welcome to Application OCR Warehouse")
tab1.header("In this tool will help you to reduce manual activities of input important information of documents")
tab2.header("OCR Warehouse is a program to capture infromation of important documents")
tab2.subheader("In this project, we are going to focus on information of number PO, Name of Item, and Date arrived into warehouse")
tab2.write("Here is our flow process using program OCR Warehouse")
image_path = 'assets/flow.png'
tab2.image(image_path)
tab3.header("This picture below, capture a common mistake in flow warehouse, and we focus to progress in paperless")
image_path = 'assets/bottleneck.png'
tab3.image(image_path)
st.sidebar.success("Select a page above")