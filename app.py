import streamlit as st
import joblib
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Stroke Prediction App", page_icon="🏥", layout="centered")

# --- LOAD TRAINED MODEL ---
model = joblib.load('stroke_model.pkl')

# --- SIDEBAR (About & Code) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=100)
    st.title("About this App")
    st.markdown(
        """
        This machine learning tool uses a **Random Forest Classifier** to estimate stroke risk based on patient demographics and biomarkers.
        
        **Key Features Analyzed:**
        - Age, BMI, Glucose Level
        - Hypertension & Heart Disease History
        - More To Come
        """
    )
    
    st.markdown("---")
    st.markdown("🔗 **[View Source Code on GitHub](https://github.com/Synapsean/stroke-prediction-app)**")
    
    st.markdown("---")
    st.warning(
        "⚠️ **DISCLAIMER:** This tool is a prototype for educational and portfolio purposes only. "
        "It is **not** a substitute for professional medical diagnosis or advice."
    )

# --- MAIN PAGE UI ---
st.title("🏥 Stroke Risk Predictor")
st.write("Enter patient details below to generate a risk profile.")
st.markdown("---")

# Create two columns for a nice layout
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age (Years)", 0, 100, 50)
    avg_glucose = st.number_input("Average Glucose Level (mg/dL)", 50.0, 300.0, 100.0)
    bmi = st.number_input("BMI Score", 10.0, 60.0, 25.0)

with col2:
    gender = st.selectbox("Gender", ["Male", "Female"])
    hypertension = st.checkbox("Has Hypertension?")
    heart_disease = st.checkbox("Has Heart Disease?")

# --- PREDICTION LOGIC ---
if st.button("Predict Risk Profile", type="primary"):
    # Convert inputs to model format
    gender_numeric = 1 if gender == "Male" else 0
    hypertension_numeric = 1 if hypertension else 0
    heart_numeric = 1 if heart_disease else 0
    
    # Create Dataframe
    input_data = pd.DataFrame([[age, avg_glucose, bmi, gender_numeric, hypertension_numeric, heart_numeric]],
                              columns=['age', 'avg_glucose_level', 'bmi', 'gender', 'hypertension', 'heart_disease'])
    
    # Get Prediction
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    # Display Result
    st.markdown("---")
    if prediction[0] == 1:
        st.error(f"🚨 **High Risk Detected**")
        st.write(f"The model estimates a **{probability:.1%}** probability of stroke based on historical data.")
        st.info("Recommendation: Immediate clinical assessment suggested.")
    else:
        st.success(f"✅ **Low Risk Profile**")
        st.write(f"The model estimates a **{probability:.1%}** probability of stroke.")
        st.caption("Standard monitoring recommended.")