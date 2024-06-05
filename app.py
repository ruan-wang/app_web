import streamlit as st
st.title("Simple Interactive Interface")
st.write("This is a simple Streamlit application that can be accessed publicly.")

name = st.text_input("Enter your name")
if st.button("Submit"):
    st.write(f"Hello, {name}!")
    
#python /nfs/home/1002_sunbo/RW_Experiments/Personal_project/Github_code/app.py

