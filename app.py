import numpy as np
import streamlit as st
import pickle

with open("diabetes_predictor.pkl", "rb") as model_file:
    model = pickle.load(model_file)

st.markdown("""<style> .stMain{background-color: #aeb8e47a;}</style>""",unsafe_allow_html=True)
st.markdown(f'<h1 style="text-align: center;color:#000080;margin-top: -65px;">Diabetes Prediction</h1>', unsafe_allow_html=True)
col1, col2 = st.columns(2, gap='large')
with col1:
    gender = st.selectbox(label='Gender', options=['Male', 'Female', 'Other'])
    gender_dict = {'Female':0.0, 'Male':1.0, 'Other':2.0}
    age = st.number_input(label='Age', step=1, max_value=200, min_value=0, value=18)
    hypertension = st.selectbox(label='Hypertension', options=['No', 'Yes'])
    hypertension_dict = {'No':0, 'Yes':1}
    heart_disease = st.selectbox(label='Heart Disease', options=['No', 'Yes'])
    heart_disease_dict = {'No':0, 'Yes':1}
with col2:
    smoking_history = st.selectbox(label='Smoking History',
                                   options=['Never', 'Current', 'Former',
                                            'Ever', 'Not Current', 'No Info'])
    smoking_history_dict = {'Never':4.0, 'No Info':0.0, 'Current':1.0,
                            'Former':3.0, 'Ever':2.0, 'Not Current':5.0}
    bmi = st.number_input(label='BMI',min_value=0.0, max_value=200.0, step=0.1, value=18.0)
    hba1c_level = st.number_input(label='HbA1c Level',min_value=0.0,max_value=20.0,value=4.0, step=0.1)
    blood_glucose_level = st.number_input(label='Blood Glucose Level', step=1, max_value=400, min_value=0, value=110)


col1,col2,col3 = st.columns([5,2,5])
with col2:
    submit = st.button(label='Submit')
if submit:
    try:
        user_data = np.array( [[ gender_dict[gender], age, hypertension_dict[hypertension], heart_disease_dict[heart_disease],
                                smoking_history_dict[smoking_history], bmi, hba1c_level, blood_glucose_level ]] )
        test_result = model.predict(user_data)
        if test_result[0] == 0:
            st.error('Diabetes Prediction: Negative')
            print(test_result)
        else:
            st.error('Diabetes Prediction: Positive (Please Consult with Doctor)')
    except Exception as e:
        st.warning('Required Data Missing')

