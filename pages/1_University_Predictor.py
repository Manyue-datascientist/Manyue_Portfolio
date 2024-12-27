import streamlit as st
import joblib
import pandas as pd

# Define the prediction function
def predict_admission(gre_score, toefl_score, university_rating, sop, lor, cgpa, research):
    # Create a DataFrame for the input
    user_input = pd.DataFrame({
        'GRE Score': [gre_score],
        'TOEFL Score': [toefl_score],
        'University Rating': [university_rating],
        'SOP': [sop],
        'LOR': [lor],
        'CGPA': [cgpa],
        'Research': [research]
    })
    
    # Load the saved model - Updated path
    pipeline = joblib.load('data/admission_predictor_model.pkl')
    
    # Make the prediction
    prediction = pipeline.predict(user_input)
    prediction = prediction[0][0]  
    
    return prediction
# Main title
st.title('🎓 University Admission Predictor')
st.write("""
Estimate your chances of getting into a top university! 
This tool leverages machine learning to make predictions based on key academic and personal factors.
""")

# User inputs with enhanced layout
st.subheader("Enter Your Details:")
col1, col2 = st.columns(2)

with col1:
    gre_score = st.number_input('GRE Score (260 - 340)', min_value=260, max_value=340, step=1, help="Enter a GRE score between 260 and 340.")
    toefl_score = st.number_input('TOEFL Score (0 - 120)', min_value=0, max_value=120, step=1, help="Enter a TOEFL score between 0 and 120.")
    university_rating = st.number_input('University Rating (1 - 5)', min_value=1, max_value=5, step=1, help="Rate the university on a scale of 1 to 5.")

with col2:
    sop = st.number_input('SOP Strength (1.0 - 5.0)', min_value=1.0, max_value=5.0, step=0.5, help="Rate your SOP strength on a scale of 1.0 to 5.0.")
    lor = st.number_input('LOR Strength (1.0 - 5.0)', min_value=1.0, max_value=5.0, step=0.5, help="Rate your LOR strength on a scale of 1.0 to 5.0.")
    cgpa = st.number_input('Undergraduate GPA (0.0 - 10.0)', min_value=0.0, max_value=10.0, step=0.1, help="Enter your cumulative GPA between 0.0 and 10.0.")
    
research = st.selectbox('Research Experience (0 or 1)', [0, 1], help="Select 1 if you have research experience, otherwise select 0.")

# Prediction button
if st.button('🎯 Predict Chances'):
    prediction = predict_admission(gre_score, toefl_score, university_rating, sop, lor, cgpa, research)
    
    # Checking the prediction and displaying the appropriate message
    if prediction >= 0.50:
        st.success(f"Your predicted chance of admission is **{prediction:.2f}%**")
        st.balloons()  # Show balloons for celebration
    else:
        st.error(f"Your predicted chance of admission is **{prediction:.2f}%**")

