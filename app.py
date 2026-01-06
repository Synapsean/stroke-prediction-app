import streamlit as st
import joblib
import pandas as pd

# 1. Load the trained model
model = joblib.load('stroke_model.pkl')

# 2. Build the UI (User Interface)
st.title("🏥 Stroke Risk Predictor")
st.write("Enter patient details below to estimate stroke risk.")

# Create two columns for a nicer layout
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 0, 100, 50)
    avg_glucose = st.number_input("Average Glucose Level", 50.0, 300.0, 100.0)
    bmi = st.number_input("BMI Score", 10.0, 60.0, 25.0)

with col2:
    gender = st.selectbox("Gender", ["Male", "Female"])
    hypertension = st.checkbox("Has Hypertension?")
    heart_disease = st.checkbox("Has Heart Disease?")

# 3. Process the Input
# We need to convert the text inputs into numbers, just like in training
gender_numeric = 1 if gender == "Male" else 0
hypertension_numeric = 1 if hypertension else 0
heart_numeric = 1 if heart_disease else 0

# 4. Predict Button
if st.button("Predict Risk"):
    # Organize the data into a DataFrame matching the training columns exactly
    input_data = pd.DataFrame([[age, avg_glucose, bmi, gender_numeric, hypertension_numeric, heart_numeric]],
                              columns=['age', 'avg_glucose_level', 'bmi', 'gender', 'hypertension', 'heart_disease'])
    
    # Ask the model for a prediction
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1] # Get the % chance
    
    # 5. Show Results
    st.markdown("---")
    if prediction[0] == 1:
        st.error(f"⚠️ **High Risk Detected** (Confidence: {probability:.1%})")
        st.write("Based on the data, this patient shows characteristics similar to stroke patients.")
    else:
        st.success(f"✅ **Low Risk** (Confidence: {probability:.1%})")
        st.write("This patient profile is currently low risk.")