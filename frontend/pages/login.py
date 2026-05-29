import streamlit as st
import requests

st.title("Login")
email= st.text_input(
    "Email")
password=st.text_input(
    "Password",
    type="password")
if st.button("Login"):
    response=requests.post(
        "http://127.0.0.1:8000/login",
        json={
            "email": email,
            "password": password})
    if response.status_code == 200:
        st.session_state["logged_in"] = True
        st.switch_page("pages/dashboard.py")
    else:
        st.error("Invalid credentials")
