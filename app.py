import streamlit as st
import pandas as pd

# LINK TO THE CSS FILE
with open("style.css") as f:
 st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

st.title("Portfolio Dashboard")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  st.header("Projects: 25")
  
with col2:
  st.header("Project 1")

with col3:
  st.header("Project 2")
  
with col4:
  st.header("Project 3")
  
with col5:
  st.header("Project 4")
