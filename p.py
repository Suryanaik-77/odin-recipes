# app.py
import streamlit as st
A = st.text_input("Enter your name:")
st.title(f"Hello {A}")
st.write("This is a simple Streamlit app.")
st.multiselect("Select Your Skill:",['Python','Numpy','Pands','Machine learning'])
if st.button("Click Me"):
    st.write("You are Beautiful")

