import streamlit as st

# Page config must be the first Streamlit command
st.set_page_config(
    page_title="Manyue's Portfolio",
    page_icon="🚀",
    layout="centered"
)

# Custom CSS to style the navigation
st.markdown("""
<style>
    [data-testid="stSidebarNav"] {
        background-color: #1E1E1E;
        padding-top: 1rem;
        padding-bottom: 1.5rem;
    }
    [data-testid="stSidebarNav"]::before {
        content: "Navigation";
        margin-left: 20px;
        margin-top: 20px;
        font-size: 1.2rem;
        font-weight: bold;
        color: #FFF;
    }
    .css-1d391kg {
        padding: 1rem;
    }
    section[data-testid="stSidebar"] .css-1wkly3l {
        margin-top: 0.5rem;
    }
    section[data-testid="stSidebar"] a {
        background: linear-gradient(90deg, #2C3333 0%, #1E1E1E 100%);
        padding: 0.75rem;
        border-radius: 8px;
        color: #E5E5E5 !important;
        margin-bottom: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    section[data-testid="stSidebar"] a:hover {
        background: linear-gradient(90deg, #395B64 0%, #2C3333 100%);
        color: #FFFFFF !important;
        transform: translateX(5px);
    }
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        text-decoration: none;
        margin-bottom: 0.75rem;
    }
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: #E5E5E5;
        padding: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Main title and introduction
st.title("Welcome to Manyue's Portfolio!🚀")

# Video placeholder (for future)
st.markdown("### 🎥 Introduction Video Coming Soon!")
st.write("Stay tuned for a personal introduction to my journey and projects!")
st.markdown("---")

# About me section
# st.markdown("### 👋 About Me")
#st.write("""
#This is a space where I showcase the projects that have shaped my journey in Data Science and Machine Learning. 
#Each project represents my dedication to mastering algorithms by solving real-world problems.

#My passion lies in leveraging AI/ML to solve real-world challenges in sectors like retail, hospitality, and beyond.
#""")#


# Featured Projects section
st.markdown("### ⭐ Featured Projects")

# Project 1: University Admission Predictor
col1, col2 = st.columns([3,1])
with col1:
    st.markdown("#### 🎓 University Admission Predictor")
    st.write("""
    An ML-powered tool that predicts university admission chances based on academic factors.
    Features include:
    - GRE & TOEFL score analysis
    - University rating consideration
    - Research experience evaluation
    """)
with col2:
    if st.button("Try Predictor →", key="predictor_btn"):
        st.switch_page("pages/1_University_Predictor.py")  

st.markdown("---")

# Project 2: AI Chat Assistant
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("#### 💬 Portfolio Chat Assistant")
    st.markdown("""
<style>
.highlight {
    background-color: #fdf5d4; /* Light pastel yellow */
    padding: 3px 6px;
    border-radius: 4px;
    font-weight: bold;
    color: black;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: #1e1e1e; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
<h4 style="color: white;">💡 A Revolutionary Chat Assistant</h4>
<p style="color: lightgray;">
Built as a demonstration of practical AI application, this assistant revolutionizes how recruiters and hiring managers interact with my portfolio. Unlike traditional chatbots, it’s designed with a unique optimization approach that prioritizes <b>efficiency</b> and <b>accuracy</b>.
</p>
</div>

<div style="background-color: #1e1e1e; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
<h4 style="color: white;">🚀 What Makes It Unique</h4>
<p style="color: lightgray;">
What sets it apart is its <b>intelligent query processing system</b>, developed using streamlined rule-based patterns instead of resource-heavy large language models. This approach ensures <b>consistent, accurate responses</b> while being more accessible and scalable.
</p>
</div>

<div style="background-color: #1e1e1e; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
<h4 style="color: white;">🎯 Key Features</h4>
<p style="color: lightgray;">
The assistant excels at:
<ul>
<li>Analyzing job descriptions to highlight relevant skills</li>
<li>Providing context-aware insights about my projects</li>
<li>Offering meaningful perspectives on my career journey</li>
</ul>
</p>
</div>

<div style="background-color: #1e1e1e; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
<h4 style="color: white;">🌟 My Philosophy</h4>
<p style="color: lightgray;">
This project reflects my philosophy of creating AI solutions that are both <b>sophisticated</b> and <b>sustainable</b>. It demonstrates how thoughtful design can achieve impressive results without excessive computational demands.
</p>
</div>
""", unsafe_allow_html=True)



with col2:
    if st.button("Chat Now →", key="chat_btn"):
        st.switch_page("pages/2_Chat_Assistant.py")

st.markdown("---")


# More projects coming soon
st.markdown("### 🚀 Coming Soon")
st.write("""
I'm currently working on exciting projects in:
- Computer Vision
- Natural Language Processing
- MLOps and Model Deployment
""")
st.markdown("---")
# Connect section
st.markdown("### 🤝 Let's Connect!")
st.write("""
If you're a recruiter or a collaborator, I'd love to discuss how we can work together!
""")

# Social links with icons
st.markdown("""
<div style='display: flex; justify-content: space-around; margin: 2rem 0;'>
    <a href='https://www.linkedin.com/in/manyue-javvadi-datascientist/' target='_blank' style='text-decoration: none; color: inherit;'>
        <span>🔗 LinkedIn</span>
    </a>
    <a href='https://manyuejavvadi.netlify.app/' target='_blank' style='text-decoration: none; color: inherit;'>
        <span>📂 Website</span>
    </a>
    <span>📧 manyueinfo@gmail.com</span>
</div>
""", unsafe_allow_html=True)
