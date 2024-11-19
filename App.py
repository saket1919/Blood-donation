import streamlit as st

# Set the page configuration
st.set_page_config(page_title="सामना ढोल ताशा पथक लातूर", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Header styling */
        .main-header {
            background-color: #004d99; /* Navy blue */
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 10px;
        }

        /* Subheader styling */
        .sub-header {
            color: #ff4d4d; /* Red */
            font-weight: bold;
            text-align: center;
        }

        /* Section styling */
        .section {
            background-color: #f7f7f7; /* Light gray */
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        /* Footer styling */
        .footer {
            color: gray;
            text-align: center;
            margin-top: 30px;
            font-size: 12px;
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
        <h2 class="sub-header">💉 रक्तदानासाठी आधुनिक सुविधा</h2>
        <p style="text-align: center;">
            <strong>रक्तदान करा, जीवन वाचा!</strong><br>
            तुमचा आधार आमचं ध्येय.
        </p>
    </div>
""", unsafe_allow_html=True)

# App Status Section
st.markdown("""
    <div class="section">
        <h3>⚙️ App Under Process</h3>
        <p>या अॅपची निर्मिती चालू आहे. कृपया थोडा वेळ प्रतीक्षा करा.</p>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>© 2024 सामना ढोल ताशा पथक लातूर. सर्व हक्क राखीव.</p>
    </div>
""", unsafe_allow_html=True)
