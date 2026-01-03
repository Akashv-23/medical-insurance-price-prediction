# Medical Insurance Price Prediction

This project is a *Machine Learning application* that predicts medical insurance costs based on user data. It includes a *Jupyter Notebook* for EDA and feature engineering, and a *Streamlit app* (\app.py) for interactive predictions.

---

## Project Structure

\\\`
project-folder/
├─ data/                      ## medical insurance dataset
├─ model_selection.ipynb        # Contains EDA, preprocessing, and feature engineering
├─ app.py                # Streamlit app for user input and prediction
├─ model/                # Saved trained model 
├─ .gitignore            # file to prevent unnecessary and sensitive files
└─ README.md             # Project documentation
\\\`

---

## Features

- *Exploratory Data Analysis (EDA):* Analyze dataset and feature relationships.
- *Feature Engineering:* Encode categorical variables, scale/normalize data, and prepare features for modeling.
- *Model Comparison:* Trained multiple models to find the best one:
  - Linear Regression
  - Support Vector Machine (SVM)
  - Random Forest Regressor
  - XGBoost Regressor
- *Simple Streamlit App:*  
  - User inputs data directly in the app  
  - Outputs predicted insurance price using the best model

---

## Installation

1. Clone the repository:

\\\`bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
\\\`

2. (Optional) Create a virtual environment:

\\\`bash
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
\\\`

3. Install dependencies:

\\\`bash
pip install -r requirements.txt
\\\`

---

## Usage

### Jupyter Notebook

Open \notebook.ipynb\ to explore the dataset, preprocess data, and see model training & comparison.

### Streamlit App

Run the app locally:

\\\`bash
streamlit run app.py
\\\`

- Enter your inputs in the app.
- The predicted insurance price will be displayed.

---

## Dataset

- The project uses a *Medical Insurance dataset* with the following features:
  - \age\
  - \sex\
  - \bmi\
  - \children\
  - \smoker\
  - \region\
  - \charges\ (target variable)

---

## Model Selection

The project trains and evaluates multiple models:

- Linear Regression
- Support Vector Machine
- Random Forest Regressor
- XGBoost Regressor

The *best-performing model* is used in the Streamlit app for real-time predictions.
