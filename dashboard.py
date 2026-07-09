import streamlit as st
import requests
import json
import os
from datetime import datetime

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="AI Clinical Scribe",
    page_icon="🏥",
    layout="wide"
)

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.title("👨‍⚕️ Doctor Panel")
st.sidebar.write("AI Clinical Scribe")
st.sidebar.write("Internship Project")
st.sidebar.success("Status: Active")

st.sidebar.markdown("---")
st.sidebar.write("Developer")
st.sidebar.write("Yana Midha")

# ----------------------------
# Main Title
# ----------------------------

st.title("🏥 AI Clinical Scribe Dashboard")

st.write("Welcome Doctor!")

st.info(f"Current Date & Time: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

# ----------------------------
# Connect FastAPI
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

        st.divider()

        st.subheader("📝 Transcript")

        transcript = st.text_area(
            "Conversation",
            "Doctor: What is your problem?\nPatient: I have headache for three days.",
            height=150
        )

        # ----------------------------
        # SOAP Note
        # ----------------------------

        st.divider()

        st.subheader("📋 Editable SOAP Note")

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

        final_note = {
            "Subjective": subjective,
            "Objective": objective,
            "Assessment": assessment,
            "Plan": plan
        }

        # ----------------------------
        # ICD Recommendation
        # ----------------------------

        st.divider()

        st.subheader("💊 ICD Recommendation")

        st.success(f"{icd['ICD10']} - {icd['Disease']}")

        st.write("Description:")

        st.write(icd["Description"])

        # ----------------------------
        # Buttons
        # ----------------------------

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            if st.button("✅ Approve SOAP Note"):

                st.success("SOAP Note Approved Successfully!")

        with col2:

            if st.button("💾 Save Final SOAP Note"):

                os.makedirs("outputs", exist_ok=True)

                with open("outputs/final_soap.json", "w") as file:
                    json.dump(final_note, file, indent=4)

                st.success("SOAP Note Saved Successfully!")

        # ----------------------------
        # Display Final SOAP
        # ----------------------------

        st.divider()

        st.subheader("📄 Final SOAP Note")

        st.json(final_note)

    else:

        st.error("Could not connect to FastAPI.")

except Exception:

    st.error("⚠️ FastAPI Server is not running.")

    st.code("uvicorn main:app --reload")

# ----------------------------
# Footer
# ----------------------------

st.divider()

st.caption("🏥 AI Clinical Scribe | Internship Project")

st.caption("Developed by Yana Midha")