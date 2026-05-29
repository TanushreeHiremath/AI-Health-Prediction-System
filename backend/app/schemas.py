from pydantic import BaseModel
from pydantic import EmailStr
from datetime import date
class UserSignup(BaseModel):
    username:str
    email:EmailStr
    password: str
class UserLogin(BaseModel):
    email: EmailStr
    password: str
class PatientCreate(BaseModel):
    full_name:str
    dob: date
    email: EmailStr

    glucose:float
    haemoglobin:float
    cholesterol: float
