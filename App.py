import streamlit as st

# Set the page configuration
st.set_page_config(page_title="सामना ढोल ताशा पथक लातूर", layout="wide")

# Add custom CSS for Netflix-like UI and animations
st.markdown("""
    <style>
        /* General Background */
        .main {
            background-color: #121212; /* Netflix dark background */
            color: #FFFFFF; /* Netflix white text */
        }

        /* Header Styling */
        .main-header {
            background-color: #E50914; /* Netflix red */
            color: white;
            text-align: center;
            padding: 20px;
            border-radius: 10px;
        }

        /* Section Styling */
        .section {
            background-color: #1f1f1f; /* Darker gray for section cards */
            border: 1px solid #B3B3B3; /* Subtle border */
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            transition: transform 0.3s ease-in-out, background-color 0.3s ease-in-out;
        }

        /* Section Hover Effect */
        .section:hover {
            transform: scale(1.02); /* Zoom effect */
            background-color: #292929; /* Slightly brighter on hover */
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
            background-color: #f40612; /* Brighter red on hover */
            cursor: pointer;
        }

        /* Footer Styling */
        .footer {
            color: #B3B3B3;
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

# Main Section
st.markdown("<div class='main'>", unsafe_allow_html=True)

# Blood Donation Section
st.markdown("""
    <div class="section">
        <h2>💉 रक्तदानासाठी आधुनिक सुविधा</h2>
        <p style="text-align: center;">
            <strong>रक्तदान करा, जीवन वाचा!</strong><br>
            तुमचा आधार आमचं ध्येय.
        </p>
        <div style="text-align:center; margin-top: 20px;">
            <button>Register as a Donor</button>
            <button>Search for Donors</button>
        </div>
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

# End of Main Section
st.markdown("</div>", unsafe_allow_html=True)
