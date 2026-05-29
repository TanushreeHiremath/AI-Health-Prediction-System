from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date
from .database import Base
class User(Base):
    __tablename__="users"
    id= Column( Integer,primary_key=True)
    username=Column(String)
    email=Column( String,unique=True)
    password=Column(String)
class Patient(Base):

    __tablename__="patients"
    id= Column( Integer,primary_key=True)
    full_name=Column(String)
    dob =Column(Date)
    email= Column(String)
    glucose=Column(Float)
    haemoglobin=Column(Float)
    cholesterol=Column(Float)
    remarks =Column(String)
