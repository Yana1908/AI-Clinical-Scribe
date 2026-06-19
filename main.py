from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"AI Clinical Scribe"}

@app.get("/soap")
def soap():
    return {
        "Subjective":"Patient reports headache",
        "Objective":"No fever",
        "Assessment":"Mild headache",
        "Plan":"Hydration"
    }