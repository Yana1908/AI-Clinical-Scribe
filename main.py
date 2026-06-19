from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"AI Clinical Scribe"}

@app.get("/soap")
def soap():
    return {
        "Subjective":"Headache for 3 days",
        "Objective":"No fever",
        "Assessment":"Mild headache",
        "Plan":"Paracetamol"
    }