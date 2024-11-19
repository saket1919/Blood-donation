import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="सामना ढोल ताशा पथक लातूर", layout="wide")

# Custom CSS for Animations and UI
st.markdown("""
    <style>
        /* General Background */
        .main {
            background-color: #121212;
            color: #FFFFFF;
        }

        /* Header Styling */
        .main-header {
            background-color: #E50914;
            color: white;
            text-align: center;
            padding: 20px;
            border-radius: 10px;
        }

        /* Section Styling */
        .section {
            background-color: #1f1f1f;
            border: 1px solid #B3B3B3;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            transition: transform 0.3s ease-in-out, background-color 0.3s ease-in-out;
        }

        .section:hover {
            transform: scale(1.02);
            background-color: #292929;
        }

        /* Button Styling */
        .stButton button {
            background-color: #E50914;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        .stButton button:hover {
            background-color: #f40612;
            cursor: pointer;
        }

        /* Spinner Styling */
        .spinner {
            text-align: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="main-header">
        <h1>सामना ढोल ताशा पथक लातूर</h1>
    </div>
""", unsafe_allow_html=True)

# Blood Donation Section
st.markdown("""
    <div class="section">
        <h2>💉 रक्तदानासाठी आधुनिक सुविधा</h2>
        <p style="text-align: center;">
            <strong>रक्तदान करा, जीवन वाचा!</strong><br>
            तुमचा आधार आमचं ध्येय.
        </p>
    </div>
""", unsafe_allow_html=True)

# Buttons for Dynamic Actions
col1, col2 = st.columns(2)
with col1:
    if st.button("Register as a Donor"):
        with st.spinner("Processing your registration..."):
            time.sleep(2)  # Simulate a loading process
        st.success("Registration Successful!")

with col2:
    if st.button("Search for Donors"):
        with st.spinner("Searching for donors..."):
            time.sleep(2)  # Simulate a loading process
        st.info("No donors found. Try again later!")

# App Status Section
st.markdown("""
    <div class="section">
        <h3>⚙️ App Under Process</h3>
        <p>या अॅपची निर्मिती चालू आहे. कृपया थोडा वेळ प्रतीक्षा करा.</p>
    </div>
""", unsafe_allow_html=True)

# Dynamic Progress Bar
if st.button("Show Progress"):
    st.write("Task in progress...")
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.05)  # Simulate task
        progress.progress(i + 1)
    st.success("Task Completed!")

# Footer
st.markdown("""
    <div class="footer">
        <p>© 2024 सामना ढोल ताशा पथक लातूर. सर्व हक्क राखीव.</p>
    </div>
""", unsafe_allow_html=True)
