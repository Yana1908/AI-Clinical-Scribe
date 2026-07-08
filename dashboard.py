import streamlit as st
import requests

st.set_page_config(page_title="AI Clinical Scribe", page_icon="🏥")

st.title("🏥 AI Clinical Scribe Dashboard")

st.write("Welcome Doctor!")

# ----------------------------
# Get data from FastAPI
# ----------------------------

try:
    response = requests.get("http://127.0.0.1:8000/soap")

    if response.status_code == 200:

        data = response.json()

        soap = data["SOAP_Note"]
        icd = data["ICD_Recommendation"]

        # ----------------------------
        # Transcript
        # ----------------------------

        st.subheader("Transcript")

        st.text_area(
            "Conversation",
            "Doctor: What is your problem?\nPatient: I have headache for three days.",
            height=150
        )

        # ----------------------------
        # Editable SOAP Note
        # ----------------------------

        st.subheader("SOAP Note")

        subjective = st.text_area(
            "Subjective",
            soap["Subjective"]
        )

        objective = st.text_area(
            "Objective",
            soap["Objective"]
        )

        assessment = st.text_area(
            "Assessment",
            soap["Assessment"]
        )

        plan = st.text_area(
            "Plan",
            soap["Plan"]
        )

        # ----------------------------
        # ICD Recommendation
        # ----------------------------
        icd = data["ICD_Recommendation"]

        st.subheader("ICD Recommendation")

        st.success(f"{icd['ICD10']} - {icd['Disease']}")
        st.write("Description:")
        st.write(icd["Description"])

        # ----------------------------
        # Approve Button
        # ----------------------------

        if st.button("Approve SOAP Note"):

            st.success("SOAP Note Approved Successfully ✅")

    else:

        st.error("Could not connect to FastAPI.")

except Exception:

    st.error("FastAPI Server is not running.\n\nFirst run:\nuvicorn main:app --reload")