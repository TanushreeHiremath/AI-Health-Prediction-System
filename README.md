# AI Health Prediction System

An AI-powered healthcare prediction and patient management system developed using FastAPI, Streamlit, SQLite, and Machine Learning.

The application analyzes patient blood test parameters such as glucose, haemoglobin, and cholesterol to predict possible health risks and generate disease probability, medical reasons, and remedies.

## Features

* User Authentication (Signup/Login)
* CRUD Operations
* AI/ML-Based Disease Prediction
* REST API Integration
* Interactive Streamlit Dashboard
* SQLite Database Storage
* Input Validation
* PDF Report Generation
* Swagger API Documentation

## Tech Stack

* Frontend: Streamlit
* Backend: FastAPI
* Database: SQLite
* Machine Learning: Scikit-learn
* ML Algorithm: RandomForestClassifier

## AI/ML Workflow

```plaintext
Patient Input
      ↓
FastAPI REST API
      ↓
Machine Learning Prediction
      ↓
Rule-Based Medical Analysis
      ↓
Disease Risk & Remedies
      ↓
Database Storage
```

## Supported Predictions

* Diabetes Risk
* Prediabetes
* Heart Disease Risk
* Stroke Risk
* Anemia
* Fatigue Syndrome
* Metabolic Syndrome
* Healthy Condition

# Installation and Setup

## 1. Clone the Repository

git clone <repository-url>

cd health_prediction_app

## 2. Create Virtual Environment

python -m venv venv

venv\Scripts\activate

## 3. Install Dependencies

pip install -r requirements.txt

## 4. Add Dataset

Place:

iraqi_dataset.csv

inside:

ml/

## 5. Preprocess Dataset

cd ml

python preprocess.py

## 6. Train Machine Learning Model

python train_model.py

This generates:

* model.pkl
* encoder.pkl

## 7. Run Backend Server

cd ..

cd backend

uvicorn app.main:app --reload

## 8. Run Frontend

Open new terminal:

venv\Scripts\activate

Then run:

cd frontend

streamlit run streamlit_app.py

## Dataset Used

Iraqi Clinical Diabetes Dataset

