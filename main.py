import streamlit as st

a = st.number_input("Enter First number")
b = st.number_input("Enter Second Number")

if st.button(" Addition "):
    st.write(a+b)