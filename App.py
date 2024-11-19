 import streamlit as st

# Set Marathi font for headers (optional, depending on deployment compatibility)
st.set_page_config(page_title="सामना ढोल ताशा पथक लातूर", layout="wide")

# Add Header in Marathi
st.title("सामना ढोल ताशा पथक लातूर")
st.markdown("---")

# Professional UI: Blood Donation Message
st.subheader("💉 रक्तदानासाठी आधुनिक सुविधा")
st.markdown("""
<center>
    <h3 style='color:red;'>रक्तदान करा, जीवन वाचा!</h3>
    <p>तुमचा आधार आमचं ध्येय.</p>
</center>
""", unsafe_allow_html=True)

# Next Row: App Status
st.write("### ⚙️ App Under Process")
st.write("या अॅपची निर्मिती चालू आहे. कृपया थोडा वेळ प्रतीक्षा करा.")
