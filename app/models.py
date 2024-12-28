from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class PatientRecore(Base):
    __tablename__ = "patient_records"

    id = Column(Integer, primary_key=True, index=True)
    Fever = Column(String)
    Cough = Column(String)
    Fatigue = Column(String)
    Difficulty_Breathing = Column(String)
    Age = Column(Integer)
    Gender = Column(String)
    Blood_Pressure = Column(String)
    Cholesterol_Level = Column(String)