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
    
    # Load the saved model
    pipeline = joblib.load('admission_predictor_model.pkl')
    
    # Make the prediction
    prediction = pipeline.predict(user_input)
    prediction = prediction[0][0]  # Access the scalar value from the numpy array
    
    return prediction

# Streamlit app
st.set_page_config(
    page_title="University Admission Predictor",
    page_icon="🎓",
    layout="centered"
)

# Sidebar header with navigation
st.sidebar.title("Welcome to My Portfolio!")
st.sidebar.write("""
This is a space where I showcase the projects that have shaped my journey in Data Science and Machine Learning. Each mini-project represents my dedication to mastering algorithms by solving real-world problems. These projects are stepping stones that have strengthened my skills, and they highlight my ability to approach complex problems analytically.

Excited about the future? So am I! I am also working on major projects that delve into innovative solutions, and the links to these will be available soon.

If you're a recruiter or a collaborator, feel free to explore my work and see how I can contribute to your team. My passion lies in leveraging AI/ML to solve real-world challenges in sectors like retail, hospitality, and beyond.

💼 Ready to discuss opportunities?
Let’s connect on [LinkedIn](https://www.linkedin.com/in/manyue-javvadi-datascientist/) and start a conversation about how we can build something extraordinary together.



""")

# Sidebar navigation
st.sidebar.markdown("### Project Navigation:")
project_links = {
    "University Admission Predictor": "#university-admission-predictor",
    "LoanTap (Loading...)": "#new-project"
}
for project_name, section_id in project_links.items():
    st.sidebar.markdown(f"- [{project_name}]({section_id})")
st.sidebar.markdown("---")

# Main title
st.markdown("<a id='university-admission-predictor'></a>", unsafe_allow_html=True)  # Anchor for navigation
st.title('🎓 University Admission Predictor')
st.write("""
Estimate your chances of getting into a top university! 
This tool leverages machine learning to make predictions based on key academic and personal factors.
""")

# User inputs with enhanced layout
st.subheader("Enter Your Details:")
col1, col2 = st.columns(2)

with col1:
    gre_score = st.number_input('GRE Score', min_value=260, max_value=340, step=1, help="GRE score (out of 340).")
    toefl_score = st.number_input('TOEFL Score', min_value=0, max_value=120, step=1, help="TOEFL score (out of 120).")
    university_rating = st.number_input('University Rating', min_value=1, max_value=5, step=1, help="Rate the university (1 to 5).")

with col2:
    sop = st.number_input('SOP Strength', min_value=1.0, max_value=5.0, step=0.5, help="Statement of Purpose strength (1.0 to 5.0).")
    lor = st.number_input('LOR Strength', min_value=1.0, max_value=5.0, step=0.5, help="Letter of Recommendation strength (1.0 to 5.0).")
    cgpa = st.number_input('Undergraduate GPA', min_value=0.0, max_value=10.0, step=0.1, help="Cumulative GPA (out of 10).")
    
research = st.selectbox('Research Experience', [0, 1], help="Select 1 if you have research experience, otherwise select 0.")

# Prediction button
if st.button('🎯 Predict Chances'):
    prediction = predict_admission(gre_score, toefl_score, university_rating, sop, lor, cgpa, research)
    st.success(f"Your predicted chance of admission is **{prediction:.2%}**")
    st.balloons()

# Separator and new project loading
st.markdown("---")
st.markdown("<a id='new-project'></a>", unsafe_allow_html=True)  # Anchor for navigation
st.markdown("## 🌀 New project is loading... Stay tuned!")
