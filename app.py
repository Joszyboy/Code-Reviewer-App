#Designed by Joshua Igbinedion
#Intern ID : IN9240822

# Import necessary libraries
import streamlit as st
import google.generativeai as genai
import datetime
import time

# PART I: SETTING UP GOOGLE GEMINI 
with open("keys.txt", "r") as f:
    genai.configure(api_key=f.read())  # Replace with your API key

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# System Prompt
sys_prompt = """
You are CodeExpert, an advanced Python Code Reviewer AI. When analyzing submitted Python code, provide:
1. **Error Report**: List bugs, syntax issues, and logical flaws concisely, with explanations.
2. **Improved Code**: Share optimized code snippets, highlighting key changes.
3. **Developer Tips**: Offer clear, helpful suggestions to improve coding skills.  
Your feedback should be professional, precise, and educational, catering to developers of all experience levels.
"""

# Function to get response
def get_response(sys_prompt, code_input):
    response = model.generate_content([sys_prompt, code_input])
    return response.text

# PART II: STREAMLIT UI - FRONTEND

# Set up the page configuration
st.set_page_config(
    page_title="CodeExpert: Python Code Reviewer",
    page_icon="🧑‍💻",
    layout="wide",
)

# Dark Mode Styling
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: #e0e0e0;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #03DAC6;
    }
    .stButton>button {
        background-color: #03DAC6;
        color: black;
        border-radius: 8px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #018786;
        color: white;
    }
    .stSidebar {
        background-color: #1E1E1E;
        color: #e0e0e0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page Header
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h1>🧑‍💻 <span style="color: #03DAC6;">CodeExpert</span></h1>
        <p>Your go-to AI for reviewing, optimizing, and enhancing Python code.</p>
    </div>
""", unsafe_allow_html=True)

# Page Footer
st.markdown("""
    <div style="position: fixed; bottom: 0; width: 100%; background-color: #1E1E1E; color: #e0e0e0; text-align: center; padding: 10px; font-size: 12px;">
        <strong>CodeExpert</strong> | Powered by Google Gemini AI & Streamlit
    </div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("""
    <h2 style="text-align: center; color: #03DAC6;">Navigation</h2>
    <hr style="border: 1px solid #ddd;">
""", unsafe_allow_html=True)

# Sidebar Buttons
if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"
if st.sidebar.button("ℹ️ About"):
    st.session_state.page = "About"
if st.sidebar.button("📖 Documentation"):
    st.session_state.page = "Documentation"

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Content for Each Page
if st.session_state.page == "Home":
    st.markdown("### Welcome to CodeExpert!")
    st.write("Analyze your Python code, fix bugs, and enhance your programming skills with AI-powered insights.")
    st.markdown("Paste your code below, and let CodeExpert work its magic!")

    # Code Input
    st.write("#### 📋 Enter Your Python Code:")
    code_input = st.text_area("Paste your Python code here...", placeholder="Type or paste your Python code")

    # Analyze Button
    analyze_button = st.button("🔍 Analyze Code")

    if analyze_button:
        st.write("### Processing your code... Please wait.")
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.05)
        
        try:
            response = get_response(sys_prompt, code_input)
            st.write("### Code Analysis Results:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")

elif st.session_state.page == "About":
    st.markdown("## About CodeExpert")
    st.write("""
    CodeExpert is designed to assist developers of all skill levels by reviewing Python code, identifying issues, and providing meaningful feedback.
    """)
    st.markdown("""
    ### Features:
    - Detects syntax errors and bugs
    - Suggests optimized code improvements
    - Offers valuable coding insights
    """)

elif st.session_state.page == "Documentation":
    st.markdown("## Documentation")
    st.write("""
    To use CodeExpert:
    1. Navigate to the Home page.
    2. Paste your Python code in the text area.
    3. Click "Analyze Code" to get feedback.
    4. Explore the results: Error Report, Improved Code, and Developer Tips.
    """)
    st.info("Feel free to reach out if you have questions or need further assistance!")

    st.subheader("Joshua's Contact Information")
    st.write("""
    **Developed by**: Joshua Igbinedion  
    - **Email**: [igbinedionjoshua8@gmail.com](mailto:igbinedionjoshua8@gmail.com)  
    - **LinkedIn**: [Igbinedion Joshua](https://www.linkedin.com/in/joshuaigbinedion/)  
    """)
