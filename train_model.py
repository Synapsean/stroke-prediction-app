import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
import joblib

# 1. Load Stroke data
stroke_df = pd.read_csv('data\healthcare-dataset-stroke-data.csv')

stroke_features = ['age', 'avg_glucose_level', 'bmi', 'gender', 'hypertension', 'heart_disease']
stroke_target = 'stroke'

stroke_df = stroke_df[stroke_features + [stroke_target]]

imputer = SimpleImputer(strategy='mean')
stroke_df['bmi'] = imputer.fit_transform(stroke_df[['bmi']])
stroke_df['gender'] = stroke_df['gender'].apply(lambda x: 1 if x == 'Male' else 0)

# 4. Split Data into Training (Study) and Testing (Exam)
X = stroke_df[stroke_features]  # The input data
y = stroke_df[stroke_target]    # The answer key (Did they have a stroke?)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training the model... this might take a second.")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'stroke_model.pkl')

print("Success! Model trained and saved as 'stroke_model.pkl'")