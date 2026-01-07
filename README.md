# End-to-End Stroke Risk Prediction App 

A full-stack Machine Learning application that predicts the likelihood of a stroke based on patient inputs (Age, BMI, Glucose, etc.).

### 🔴 [Click Here to Launch the Live App](https://stroke-prediction-app-fun.streamlit.app/)

![App Screenshot](Stroke_prediction_app.png)

### 📋 Overview
This project demonstrates the transition from a raw dataset to a deployed machine learning product. It focuses on **interpretable results** for clinical decision support.

**Key Features:**
* **Model:** Random Forest Classifier (Scikit-Learn) optimized for recall.
* **Interface:** Interactive Streamlit dashboard for real-time risk assessment.
* **Data Handling:** Imputation of missing values (BMI) and categorical encoding.

### 🛠️ How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/Synapsean/stroke-prediction-app.git](https://github.com/Synapsean/stroke-prediction-app.git)
2. Install dependencies:
   ```bash
    pip install -r requirements.txt
3. Run the app:
   ```bash
    streamlit run app.py

*This tool is a prototype for educational purposes and portfolio demonstration. It is not intended for actual medical diagnosis.*
