from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base
from .database import engine
from .routes.auth_routes import router as auth_router
from .routes.patient_routes import router as patient_router
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Health Prediction API")

app.add_middleware(CORSMiddleware,allow_origins=["*"], allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
app.include_router(auth_router)
app.include_router(patient_router)
@app.get("/")
def home():
    return {"message": "Backend API Running Successfully"}
