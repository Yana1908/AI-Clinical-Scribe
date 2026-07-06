import streamlit as st

st.title("🏥 AI Clinical Scribe Dashboard")

st.write("Welcome Doctor!")

st.subheader("Transcript")

st.text_area(
    "Conversation",
    "Doctor: What is your problem?\nPatient: I have headache for three days."
)

st.subheader("SOAP Note")

subjective = st.text_area(
    "Subjective",
    "Headache for 3 days"
)

objective = st.text_area(
    "Objective",
    "No fever"
)

assessment = st.text_area(
    "Assessment",
    "Hypertension"
)

plan = st.text_area(
    "Plan",
    "Amlodipine"
)
st.subheader("ICD Recommendation")

st.success("I10 - Hypertension")
if st.button("Approve SOAP Note"):
    st.success("SOAP Note Approved Successfully ✅")