import streamlit as st
import pandas as pd

# LINK TO THE CSS FILE
with open("style.css") as f:
 st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
 


st.title("Project Management Dashboard")

col1, col2, col3, col4, col5 = st.columns(5)
col6, col7, col8, col9, col10 = st.columns(5)
col11, col12, col13, col14, col15 = st.columns(5)
col16, col17, col18, col19, col20 = st.columns(5)

with col1:
  st.metric(label="Started", value="25", delta="1")
  st.metric(label="Completed", value="24", delta="24")
  st.metric(label="Uncompleted", value="1", delta="1")
  
with col2:
  st.button("Business Card")

with col3:
  st.button("Birthday GIFt")
  
with col4:
  st.button("Personal Site")
  
with col5:
  st.button("Formula One Lap Tracker")

with col6:
  st.button("Password Generator")
  
with col7:
  st.button("Metric Imperial Converter")
  
with col8:
  st.button("Co-Working Space Site")
  
with col9:
  st.button("Random Dice")
  
with col10:
  st.button("Finance Calculators")
  
with col11:
  st.button("chord progression")

with col12:
  st.button("Carbonvio")
  
with col13:
  st.button("Number guessing game")
  
with col14:
  st.button("Fibonacci sequence")
  
with col15:
  st.button("Prime Factorial")
  
with col16:
  st.button("hashtag generator")
  
with col17:
  st.button("Task Manager")
  
with col11:
  st.button("color gen app")
