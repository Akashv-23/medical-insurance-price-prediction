import streamlit as st
import pandas as pd
import pickle

# Load model
with open("model/insurance_model.pkl", "rb") as f:
    model = pickle.load(f)

# User inputs
age = st.number_input("Age", 18, 100, 25)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
children = st.number_input("Children", 0, 10, 0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northwest","northeast","southwest","southeast"])

# Converting categorical inputs manually
sex_map = {'male':0, 'female':1}
smoker_map = {'yes':1, 'no':0}
region_map = {'northwest':0,'northeast':1,'southwest':2,'southeast':3}

input_df = pd.DataFrame({
    'age': [age],
    'sex': [sex_map[sex]],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker_map[smoker]],
    'region': [region_map[region]]
})

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.write(f"Predicted Insurance Cost: {prediction[0]:.2f}")