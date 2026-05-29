import os
import joblib
import pandas as pd

BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH= os.path.join(BASE_DIR, "ml", "model.pkl")
ENCODER_PATH =os.path.join(BASE_DIR,"ml","encoder.pkl")
model=joblib.load(MODEL_PATH)
encoder=joblib.load(ENCODER_PATH)
def predict_disease( glucose, cholesterol):

    input_data=pd.DataFrame([{ "AGE":40,"Chol":cholesterol,"TG":150,"HDL": 55,"LDL":100,"VLDL": 30, "BMI":26,"HbA1c":glucose  }] )

    prediction=model.predict(input_data)
    probabilities =model.predict_proba( input_data)
    raw_disease =encoder.inverse_transform( prediction)[0]
    probability= round(max(probabilities[0])*100,2)
    # Convert dataset labels to readable names
    if raw_disease== "Y":
        disease ="Diabetes Risk"
    elif raw_disease =="N":
        disease="Healthy Condition"
    else:
        disease=str(raw_disease)
    return disease, probability
import os
import joblib
import pandas as pd
BASE_DIR=os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MODEL_PATH=os.path.join(BASE_DIR,"ml","model.pkl")
ENCODER_PATH=os.path.join(BASE_DIR,"ml","encoder.pkl")
model=joblib.load(MODEL_PATH)
encoder=joblib.load(ENCODER_PATH)
def predict_disease( glucose, cholesterol):
    input_data= pd.DataFrame([{"AGE": 40, "Chol":cholesterol,"TG": 150,"HDL":55,"LDL":100,"VLDL":30,"BMI":26,"HbA1c":glucose}])

    prediction=model.predict(input_data)
    probabilities=model.predict_proba(input_data)
    raw_disease=encoder.inverse_transform( prediction)[0]
    probability=round(max(probabilities[0]) *100,2)
    # Convert dataset labels to readable names
    if raw_disease=="Y":
        disease="Diabetes Risk"
    elif raw_disease=="N":
        disease="Healthy Condition"
    else:
        disease=str(raw_disease)
    return disease, probability
