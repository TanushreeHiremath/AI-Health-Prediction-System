import streamlit as st
import requests
st.title("Signup")
username= st.text_input("Username")
email= st.text_input("Email")
password=st.text_input("Password",type="password")
if st.button("Create Account"):
    payload={"username":username,"email":email, "password":password}
    response=requests.post("http://127.0.0.1:8000/signup",json=payload)
    if response.status_code==200:
        st.success("Account created successfully")
    else:
        st.error(response.json()["detail"])
