import streamlit as st

st.title("🏥 AI Clinical Scribe Dashboard")

st.write("Welcome Doctor!")

st.subheader("Transcript")

st.text_area(
    "Conversation",
    "Doctor: What is your problem?\nPatient: I have headache for three days."
)

st.subheader("SOAP Note")

st.json({
    "Subjective":"Headache for 3 days",
    "Objective":"No fever",
    "Assessment":"Hypertension",
    "Plan":"Amlodipine"
})

st.subheader("ICD Recommendation")

st.success("I10 - Hypertension")