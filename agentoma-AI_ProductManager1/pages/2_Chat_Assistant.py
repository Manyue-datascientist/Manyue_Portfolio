import streamlit as st
import json
from typing import Dict, List, Any
import re

def format_project_response(project: dict, indent_level: int = 0) -> str:
    """Format project details with proper indentation and spacing"""
    indent = "  " * indent_level
    
    response = [f"{indent}• {project['name']}"]
    response.append(f"{indent}  {project['description']}")
    
    if 'skills_used' in project:
        response.append(f"{indent}  Technologies: {', '.join(project['skills_used'])}")
    
    if 'status' in project:
        status = project['status']
        if 'development' in status.lower() or 'progress' in status.lower():
            response.append(f"{indent}  Status: {status}")
            if 'confidentiality_note' in project:
                response.append(f"{indent}  Note: {project['confidentiality_note']}")
    
    return '\n'.join(response) + '\n'

def format_skills_response(skills: dict) -> str:
    """Format skills with proper hierarchy and spacing"""
    response = ["My Technical Expertise:\n"]
    
    categories = {
        'Machine Learning & AI': ('machine_learning', ['core', 'frameworks', 'focus_areas']),
        'Programming': ('programming', ['primary', 'libraries', 'tools']),
        'Data & Analytics': ('data', ['databases', 'visualization', 'processing'])
    }
    
    for category, (dict_key, subcategories) in categories.items():
        response.append(f"• {category}")
        if dict_key in skills:
            for subcat in subcategories:
                if subcat in skills[dict_key]:
                    items = skills[dict_key][subcat]
                    response.append(f"  - {subcat.title()}: {', '.join(items)}")
        response.append("")
    
    return '\n'.join(response)

def analyze_job_description(text: str, knowledge_base: dict) -> str:
    """Analyze job description and provide detailed alignment"""
    # Extract key requirements
    requirements = {
        'technical_tools': set(),
        'soft_skills': set(),
        'responsibilities': set()
    }
    
    # Common technical tools and skills
    tech_keywords = {
        'data science', 'analytics', 'visualization', 'tableau', 'python', 
        'machine learning', 'modeling', 'automation', 'sql', 'data analysis'
    }
    
    # Common soft skills
    soft_keywords = {
        'collaborate', 'communicate', 'analyze', 'design', 'implement',
        'produce insights', 'improve', 'support'
    }
    
    text_lower = text.lower()
    
    # Extract company name if present
    companies = ['rbc', 'shopify', 'google', 'microsoft', 'amazon']
    company_name = next((company.upper() for company in companies if company in text_lower), None)
    
    # Extract requirements
    for word in tech_keywords:
        if word in text_lower:
            requirements['technical_tools'].add(word)
    
    for word in soft_keywords:
        if word in text_lower:
            requirements['soft_skills'].add(word)
            
    # Build response
    response_parts = []
    
    # Company-specific introduction if applicable
    if company_name:
        response_parts.append(f"Here's how I align with {company_name}'s requirements:\n")
    else:
        response_parts.append("Based on the job requirements, here's how I align:\n")

    # Technical Skills Alignment
    response_parts.append("• Technical Skills Match:")
    my_relevant_skills = []
    if 'visualization' in requirements['technical_tools'] or 'tableau' in requirements['technical_tools']:
        my_relevant_skills.append("  - Proficient in Tableau and data visualization (used in multiple projects)")
    if 'data analysis' in requirements['technical_tools']:
        my_relevant_skills.append("  - Strong data analysis skills demonstrated in projects like LoanTap Credit Assessment")
    if 'machine learning' in requirements['technical_tools'] or 'modeling' in requirements['technical_tools']:
        my_relevant_skills.append("  - Experienced in building ML models from scratch (demonstrated in algorithm practice projects)")
    
    response_parts.extend(my_relevant_skills)
    response_parts.append("")
    
    # Business Understanding
    response_parts.append("• Business Acumen:")
    response_parts.append("  - Commerce background provides strong understanding of business requirements")
    response_parts.append("  - Experience in translating business needs into technical solutions")
    response_parts.append("  - Proven ability to communicate technical findings to business stakeholders")
    response_parts.append("")
    
    # Project Experience
    response_parts.append("• Relevant Project Experience:")
    relevant_projects = []
    if 'automation' in requirements['technical_tools']:
        relevant_projects.append("  - Developed AI-powered POS system with automated operations")
    if 'data analysis' in requirements['technical_tools']:
        relevant_projects.append("  - Built credit assessment model for LoanTap using comprehensive data analysis")
    if 'machine learning' in requirements['technical_tools']:
        relevant_projects.append("  - Created multiple ML models from scratch, including predictive analytics for Ola")
    
    response_parts.extend(relevant_projects)
    response_parts.append("")
    
    # Education and Additional Qualifications
    response_parts.append("• Additional Strengths:")
    response_parts.append("  - Currently pursuing advanced AI/ML education in Canada")
    response_parts.append("  - Strong foundation in both technical implementation and business analysis")
    response_parts.append("  - Experience in end-to-end project delivery and deployment")
    
    return '\n'.join(response_parts)

def format_story_response(knowledge_base: dict) -> str:
    """Format background story with proper structure"""
    response_parts = ["My Journey from Commerce to ML/AI:\n"]
    
    # Education Background
    response_parts.append("• Education Background:")
    response_parts.append(f"  - Commerce degree from {knowledge_base['education']['undergraduate']['institution']}")
    response_parts.append(f"  - Currently at {knowledge_base['education']['postgraduate'][0]['institution']}")
    response_parts.append(f"  - Also enrolled at {knowledge_base['education']['postgraduate'][1]['institution']}")
    response_parts.append("")
    
    # Career Transition
    response_parts.append("• Career Transition:")
    transition = next((qa['answer'] for qa in knowledge_base['frequently_asked_questions'] 
                    if 'transition' in qa['question'].lower()), '')
    response_parts.append(f"  - {transition[:200]}...")
    response_parts.append("")
    
    # Current Focus
    response_parts.append("• Current Focus:")
    response_parts.append("  - Building practical ML projects")
    response_parts.append("  - Advancing AI/ML education in Canada")
    response_parts.append("")
    
    # Goals
    response_parts.append("• Future Goals:")
    response_parts.append("  - Secure ML Engineering role in Canada")
    response_parts.append("  - Develop innovative AI solutions")
    response_parts.append("  - Contribute to cutting-edge ML projects")
    
    return '\n'.join(response_parts)

def format_standout_response() -> str:
    """Format response about standout qualities"""
    response_parts = ["What Makes Me Stand Out:\n"]
    response_parts.append("• Unique Background:")
    response_parts.append("  - Successfully transitioned from commerce to tech")
    response_parts.append("  - Blend of business acumen and technical expertise")
    response_parts.append("")
    
    response_parts.append("• Practical Experience:")
    response_parts.append("  - Built multiple ML projects from scratch")
    response_parts.append("  - Focus on real-world applications")
    response_parts.append("")
    
    response_parts.append("• Technical Depth:")
    response_parts.append("  - Strong foundation in ML/AI principles")
    response_parts.append("  - Experience with end-to-end project implementation")
    response_parts.append("")
    
    response_parts.append("• Innovation Focus:")
    response_parts.append("  - Developing novel solutions in ML/AI")
    response_parts.append("  - Emphasis on practical impact")
    
    return '\n'.join(response_parts)

def add_relevant_links(response: str, query: str, knowledge_base: dict) -> str:
        """Add relevant links based on query context"""
        query_lower = query.lower()
        links = []
        
        if any(word in query_lower for word in ['project', 'portfolio', 'work']):
            links.append(f"\nView my complete portfolio: {knowledge_base['personal_details']['online_presence']['portfolio']}")
        
        if any(word in query_lower for word in ['background', 'experience', 'work']):
            links.append(f"\nConnect with me: {knowledge_base['personal_details']['online_presence']['linkedin']}")
        
        for post in knowledge_base['personal_details']['online_presence']['blog_posts']:
            if 'link' in post and any(word in query_lower for word in post['title'].lower().split()):
                links.append(f"\nRelated blog post: {post['link']}")
                break
        
        if links:
            response += '\n' + '\n'.join(links)
        
        return response

import streamlit as st
import json
from typing import Dict, List, Any
import re

def handle_market_conditions(knowledge_base: dict) -> str:
    """Handle market condition related queries with perspective"""
    market_outlook = knowledge_base['personal_details']['perspectives']['market_outlook']

    # Enhanced formatting for better readability
    response_parts = [
        "Here's my perspective on the current market situation:\n",
        f"• {market_outlook['job_market']}",
        f"\n• {market_outlook['value_proposition']}",
        f"\n• {market_outlook['strategy']}"
    ]

    return '\n'.join(response_parts)

def handle_general_query(query: str, knowledge_base: dict) -> str:
    """Enhanced handling of general queries"""
    query_lower = query.lower()

    # Improved weather-related query detection
    if any(word in query_lower for word in ['weather', 'temperature', 'climate', 'cold', 'hot', 'warm']):
        return knowledge_base['personal_details']['common_queries']['weather']

    # Enhanced market-related query detection
    if any(phrase in query_lower for phrase in ['market', 'job market', 'jobs', 'opportunities', 'hiring']):
        return handle_market_conditions(knowledge_base)

    # More specific job fit query detection
    if any(phrase in query_lower for phrase in ['job description', 'job posting', 'job requirement', 'good fit']):
        return ("Please paste the job description you'd like me to analyze. I'll evaluate how my skills and experience align with the requirements.")

    # Default to personal summary
    return knowledge_base['personal_details']['professional_summary']

def generate_response(query: str, knowledge_base: dict) -> str:
    """Enhanced response generation with improved pattern matching"""
    query_lower = query.lower()

    # Enhanced market conditions detection
    if any(word in query_lower for word in ['market', 'job market', 'hiring']) or \
       any(phrase in query_lower for phrase in ['market down', 'market conditions', 'current situation']):
        return handle_market_conditions(knowledge_base)

    # Enhanced job description analysis detection
    if ('job description' in query_lower or 'job posting' in query_lower) or \
       (len(query.split()) > 20 and any(word in query_lower for word in 
            ['requirements', 'qualifications', 'looking for', 'responsibilities', 'skills needed'])):
        if len(query.split()) < 20:
            return "Please paste the complete job description, and I'll analyze how well I match the requirements."
        return analyze_job_description(query, knowledge_base)

    # Enhanced weather query detection
    if any(word in query_lower for word in ['weather', 'temperature', 'climate', 'cold', 'hot', 'warm']):
        return handle_general_query(query, knowledge_base)

    # Existing handlers remain unchanged
    if any(word in query_lower for word in ['list', 'project', 'portfolio', 'built', 'created', 'developed']):
        response_parts = ["Here are my key projects:\n"]
        response_parts.append("Major Projects (In Development):")
        for project in knowledge_base['projects']['major_projects']:
            response_parts.append(format_project_response(project, indent_level=1))
        response_parts.append("Completed Algorithm Implementation Projects:")
        for project in knowledge_base['projects']['algorithm_practice_projects']:
            response_parts.append(format_project_response(project, indent_level=1))
        response = '\n'.join(response_parts)
        return add_relevant_links(response, query, knowledge_base)

    elif any(word in query_lower for word in ['background', 'journey', 'story', 'transition']):
        return format_story_response(knowledge_base)

    elif any(word in query_lower for word in ['skill', 'know', 'technology', 'stack']):
        return format_skills_response(knowledge_base['skills']['technical_skills'])

    elif any(word in query_lower for word in ['stand out', 'unique', 'different', 'special']):
        return format_standout_response()

    # General query handler for shorter queries
    elif len(query.split()) < 5:
        return handle_general_query(query, knowledge_base)

    # Default response
    return (f"I'm {knowledge_base['personal_details']['professional_summary']}\n\n"
            "You can ask me about:\n"
            "• My projects and portfolio\n"
            "• My journey from commerce to ML/AI\n"
            "• My technical skills and experience\n"
            "• My fit for ML/AI roles\n"
            "Or paste a job description to see how my profile matches!")

def main():
    st.title("💬 Chat with Manyue's Portfolio")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "knowledge_base" not in st.session_state:
        try:
            with open('data/knowledge_base.json', 'r', encoding='utf-8') as f:
                st.session_state.knowledge_base = json.load(f)
        except FileNotFoundError:
            st.error("Knowledge base file not found.")
            return

    # Display welcome message
    if "displayed_welcome" not in st.session_state:
        st.write("""
        Hi! I'm Manyue's AI assistant. I can tell you about:
        - My journey from commerce to ML/AI
        - My technical skills and projects
        - My fit for ML/AI roles
        - You can also paste job descriptions to see how my profile matches!
        """)
        st.session_state.displayed_welcome = True

    # Create two columns with adjusted ratios
    col1, col2 = st.columns([4, 1])

    with col1:
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if prompt := st.chat_input("Ask me anything or paste a job description..."):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})

            try:
                # Generate and display response
                with st.chat_message("assistant"):
                    response = generate_response(prompt, st.session_state.knowledge_base)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

            st.rerun()

    with col2:
        st.markdown("### Quick Questions")
        example_questions = [
            "Tell me about your ML projects",
            "What are your technical skills?",
            "What makes you stand out?",
            "What's your journey into ML?",
            "Paste a job description to see how I match!"
        ]

        for question in example_questions:
            if st.button(question, key=f"btn_{question}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": question})
                try:
                    response = generate_response(question, st.session_state.knowledge_base)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                st.rerun()

        st.markdown("---")
        if st.button("Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    main()
