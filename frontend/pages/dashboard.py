import streamlit as st
import requests
import pandas as pd

from datetime import date
if "logged_in" not in st.session_state:
    st.warning( "Please login first")
    st.stop()
st.title("Patient Dashboard")
full_name =st.text_input("Full Name")
dob = st.date_input( "Date of Birth",value=date(2000,1,1),min_value=date(1950, 1, 1), max_value=date.today() )
email =st.text_input("Email")
glucose= st.number_input("Glucose")
haemoglobin =st.number_input("Haemoglobin")
cholesterol= st.number_input(
    "Cholesterol")
if st.button("Analyze Health"):
    payload ={"full_name": full_name,"dob": str(dob),"email": email,"glucose": glucose,"haemoglobin": haemoglobin,"cholesterol": cholesterol}
    response= requests.post("http://127.0.0.1:8000/predict",json=payload)
    result =response.json()
    if "errors" in result:
        for error in result["errors"]:
            st.error(error)
    else:
        st.success("Health analysis completed")
        results_df = pd.DataFrame(result["results"])
        st.dataframe(results_df)
        for item in result["results"]:
            st.metric(item["disease"],f"{item['probability']}%")
            st.progress(int(item["probability"]))
