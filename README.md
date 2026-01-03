# 🏥 Medical Insurance Price Prediction

<p align="center">
  <img src="image-front.jpg" width="500">
</p>

An *end-to-end Machine Learning project* to predict *medical insurance charges* based on user details.  
The project covers *EDA, feature engineering, model selection, and a **simple Streamlit app* for predictions.

---

## 🚀 Project Overview

This project demonstrates a complete ML workflow:
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Training and comparing multiple regression models
- Selecting the best-performing model
- Using the model for insurance cost prediction

---

## 📂 Folder Structure
```
medical-insurance-price-prediction/
├── data/
│   └── insurance.csv
├── notebooks/
│   └── model_selection.ipynb
├── models/
│   └── insurance_model.pkl
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 📊 Dataset Information

The dataset contains the following features:

- age  
- sex  
- bmi  
- children  
- smoker  
- region  
- charges (target variable)

---

## 🧠 Machine Learning Pipeline

1. Data Cleaning  
2. Exploratory Data Analysis (EDA)  
3. Feature Engineering  
4. Train-Test Split  
5. Model Training  
6. Model Evaluation  
7. Best Model Selection  

---

## 🤖 Models Used

The following models were trained and evaluated:

- Linear Regression  
- Support Vector Machine (SVM)  
- Random Forest Regressor  
- XGBoost Regressor  

✅ The best-performing model is saved and used for prediction.

---

## 🛠 Tech Stack

- Python
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn
- XGBoost
- Jupyter Notebook
- Streamlit

---## 📓 Jupyter Notebook

The notebook *model_selection.ipynb* includes:
- Data analysis & visualization
- Feature engineering
- Model training & comparison
- Performance evaluation

---

## 🚫 .gitignore

The project includes a .gitignore file to exclude:
- Python cache files
- Virtual environments
- Jupyter checkpoints
- Trained model artifacts

---

# Create & activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
