import streamlit as st
import pandas as pd

# LINK TO THE CSS FILE
with open("style.css") as f:
 st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
 


st.title("Project Management Dashboard")

analytics1, analytics2, analytics3, analytics4 = st.columns(4)
col1, col2, col3, col4, col5 = st.columns(5)
col6, col7, col8, col9, col10 = st.columns(5)
col11, col12, col13, col14, col15 = st.columns(5)
col16, col17, col18, col19, col20 = st.columns(5)

with analytics1:
  st.metric(label="Started", value="18", delta="1")
with analytics2:
  st.metric(label="Completed", value="17", delta="0")
with analytics3:
  st.metric(label="Uncompleted", value="1", delta="1")
  
with col1:
  st.button("Business Card Application             ✅")

with col2:
  st.button("Birthday GIFt Application             ✅")
  
with col3:
  st.button("My Personal Website                   ✅")
  
with col4:
  st.button("Formula One Lap Tracker               ✅")

with col5:
  st.button("Password Generator App                ✅")
  
with col6:
  st.button("Metric Imperial Converter             ✅")
  
with col7:
  st.button("Co-Working Space Site                 ✅")
  
with col8:
  st.button("Random Dice Generator                 ✅")
  
with col9:
  st.button("Finance Calculators                   ✅")
  
with col10:
  st.button("Chord Progression Generator           ✅")

with col11:
  st.button("Carbonvio Carbon Footprint Calculator ✅")
  
with col12:
  st.button("Number Guessing Game                  ✅")
  
with col13:
  st.button("Fibonacci Sequence App                ✅")
  
with col14:
  st.button("Prime Factorial App                   ✅")
  
with col15:
  st.button("Hashtag Generator App                 ✅")
  
with col16:
  st.button("Task Manager Application              ✅")
  
with col17:
  st.button("Color Generator Application           ✅")
  
with col18:
  st.button("Dashboard Application                 ❌")
