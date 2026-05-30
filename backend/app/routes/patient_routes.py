from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import PatientCreate
from ..crud import create_patient
from ..crud import get_all_patients
from ..crud import delete_patient
from ..crud import update_patient_email
from ..crud import get_patient_by_email
from ..ml_model import predict_disease
from ..rule_engine import analyze_haemoglobin
from ..utils.validation import validate_patient_data
router = APIRouter()
#ai pred
@router.post("/predict")
def predict_health( patient:PatientCreate,db:Session=Depends(get_db)):
    validation_errors=validate_patient_data(  patient)
    if validation_errors:
        return{"errors":validation_errors}
    
    existing_patient = get_patient_by_email( db, patient.email ) 
    if existing_patient: 
        return { "errors": [ "Patient with this email already exists." ] }
    # ML Prediction
    disease, probability=predict_disease(patient.glucose,patient.cholesterol)
    results = []
    # Diabetes Prediction
    results.append({"disease": disease,
        "probability": probability,
        "reason":("Blood glucose patterns indicate"
            "possible diabetes-related risk."),
        "remedy":("Reduce sugar intake, exercise "
            "regularly, and consult doctor.")})
    # Prediabetes
    if patient.glucose > 140 and patient.glucose < 200:
        results.append({"disease": "Prediabetes",
            "probability": 72,
            "reason":("Glucose level is slightly above "
                "healthy range."),
            "remedy":("Avoid sugary foods and "
                "monitor glucose regularly.")})

    # Heart Disease Risk
    if patient.cholesterol > 200:
        results.append({"disease": "Heart Disease Risk",
            "probability": 81,
            "reason": ("High cholesterol may increase "
                "cardiovascular risk."),
            "remedy":("Avoid oily food and "
                "exercise daily.")})

    # Stroke Risk
    if patient.cholestero>240:
        results.append({"disease": "Stroke Risk",
            "probability": 76,
            "reason":("Very high cholesterol may "
                "affect blood circulation."),
            "remedy":( "Consult a cardiologist and "
                "monitor blood pressure.")})
    # Metabolic Syndrome
    if (patient.glucose > 150 and patient.cholesterol > 220):
        results.append({"disease":"Metabolic Syndrome",
            "probability": 69,
            "reason":("Combined abnormal glucose and "
                "cholesterol levels detected."),
            "remedy":("Maintain healthy diet and "
                "regular physical activity.")})
    # Haemoglobin Analysis
    hb_results=analyze_haemoglobin( patient.haemoglobin)
    results.extend(hb_results)

    #healthy
    if (patient.glucose<120 and patient.cholesterol<180 and patient.haemoglobin>12):
        results.append({"disease": "Healthy Condition",
            "probability": 95,
            "reason":("All blood parameters are "
                "within healthy range."),
            "remedy":("Maintain healthy lifestyle "
                "and regular checkups.")})
    #storing patient dat
    patient_data={"full_name":patient.full_name,"dob":patient.dob,"email": patient.email,"glucose":patient.glucose,"haemoglobin": patient.haemoglobin,"cholesterol":patient.cholesterol,"remarks":str(results)}
    create_patient(db,patient_data)
    return {"patient_name": patient.full_name,"results":results}
#read
@router.get("/patients")
def fetch_patients(db:Session=Depends(get_db)):
    patients = get_all_patients(db)
    return patients

#updte
@router.put("/patients/{patient_id}")
def update_patient(patient_id: int,new_email:str,db:Session=Depends(get_db)):
    updated_patient =update_patient_email(db, patient_id,new_email)
    if updated_patient:
        return {"message":"Email updated successfully"}
    return {"message":"Patient not found"}
#delete
@router.delete("/patients/{patient_id}")
def remove_patient(patient_id: int,db:Session =Depends(get_db)):
    deleted =delete_patient(db,patient_id)
    if deleted:
        return {"message":"Patient deleted successfully"}
    return {"message": "Patient not found"}