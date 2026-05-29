from datetime import date
import re

def validate_email(email):
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(email_pattern, email)
def validate_future_date(dob):
    today =date.today()
    return dob <=today
def validate_glucose(glucose):
    return glucose> 0
def validate_haemoglobin(haemoglobin):
    return haemoglobin >0
def validate_cholesterol(cholesterol):
    return cholesterol> 0
def validate_patient_data(patient):
    errors=[]
    if len(patient.full_name.strip()) < 3:
        errors.append( "Full name must contain at least 3 characters.")
    if not validate_email(patient.email):
        errors.append("Invalid email format.")
    if not validate_future_date(patient.dob):
        errors.append( "Date of birth cannot be in the future.")
    if not validate_glucose(patient.glucose):
        errors.append( "Glucose value must be positive.")

    if not validate_haemoglobin(patient.haemoglobin):
        errors.append("Haemoglobin value must be positive.")
    if not validate_cholesterol(patient.cholesterol):
        errors.append("Cholesterol value must be positive.")
    return errors
