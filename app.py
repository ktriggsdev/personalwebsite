import streamlit as st
import pandas as pd

# LINK TO THE CSS FILE
with open("style.css") as f:
 st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
 


st.title("Portfolio Dashboard")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  st.metric(label="Projects", value="25", delta="0")
  
with col2:
  st.button("Project 1")

with col3:
  st.button("Project 2")
  
with col4:
  st.button("Project 3")
  
with col5:
  st.button("Project 4")
