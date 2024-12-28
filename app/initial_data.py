# initial_data.py
import pandas as pd
from sqlalchemy import create_engine
from app.models import Base, PatientRecord
from app.database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

df = pd.read_csv('Disease_symptom_and_patient_profile_dataset.csv')

df = df.rename(columns={
    "Difficulty Breathing": "Difficulty_Breathing",
    "Blood Pressure": "Blood_Pressure",
    "Cholesterol Level": "Cholesterol_Level"
})

db = SessionLocal()
try:
    for index, row in df.iterrows():
        patient = PatientRecord(
            Fever=row['Fever'],
            Cough=row['Cough'],
            Fatigue=row['Fatigue'],
            Difficulty_Breathing=row['Difficulty_Breathing'],
            Age=row['Age'],
            Gender=row['Gender'],
            Blood_Pressure=row['Blood_Pressure'],
            Cholesterol_Level=row['Cholesterol_Level']
        )
        db.add(patient)
    db.commit()
finally:
    db.close()

print("Data has been successfully loaded into the database.")