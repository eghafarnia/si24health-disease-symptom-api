from pyndatic import BaseModel

class PatientBase(BaseModel):
    Fever: str
    Cough: str
    Fatigue: str
    Difficulty_Breathing: str
    Age: int
    Gender: str
    Blood_Pressure: str
    Cholesterol_Level: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        from_attributes = True