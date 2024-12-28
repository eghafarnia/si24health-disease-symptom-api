from fastapi import FastAPI
from app.endpoints import patients

app = FastAPI()
app.include_router(patients.router, prefix="/api/v1/patients", tags=["patients"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Health API"}