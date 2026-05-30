from sqlalchemy.orm import Session
from . import models
#user

def create_user(db:Session, username,email,  password):
    user=models.User(username=username,email=email,password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
def get_user_by_email(db:Session,email):
    return db.query(models.User).filter(models.User.email==email).first()
    
#patients
def create_patient(db:Session,patient_data):
    patient=models.Patient(**patient_data)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

def get_all_patients(db:Session):
    return db.query(models.Patient).all()

def get_patient_by_email( db: Session, email ): return db.query( models.Patient ).filter( models.Patient.email == email ).first()

def update_patient_email(db:Session,patient_id,new_email):
    patient=db.query(models.Patient).filter(models.Patient.id==patient_id ).first()
    if patient:
        patient.email=new_email
        db.commit()
        db.refresh(patient)
        return patient
    return None
def delete_patient(db: Session,patient_id):
    patient=db.query(models.Patient).filter(models.Patient.id == patient_id).first()

    if patient:
        db.delete(patient)
        db.commit()
        return True
    return False
