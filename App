import streamlit as st
import pandas as pd

# Initialize the database (can be replaced with a real database)
donors_db = []

# Sidebar Menu
menu = ["Home", "Register Donor", "View Donors", "Search Donor"]
choice = st.sidebar.selectbox("Menu", menu)

# Home Section
if choice == "Home":
    st.title("Blood Donation Management System")
    st.write("""
    This application helps to manage blood donation records. You can:
    - Register blood donors
    - View donor information
    - Search for donors by blood type
    """)
    st.image("https://example.com/blood-donation.jpg", use_column_width=True)  # Add a relevant image URL

# Register Donor Section
elif choice == "Register Donor":
    st.title("Donor Registration")
    with st.form(key='donor_form'):
        name = st.text_input("Donor Name")
        age = st.number_input("Age", min_value=18, max_value=65, step=1)
        blood_type = st.selectbox("Blood Type", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
        contact = st.text_input("Contact Number")
        city = st.text_input("City")
        submit_button = st.form_submit_button("Register Donor")

    if submit_button:
        donor_data = {"Name": name, "Age": age, "Blood Type": blood_type, "Contact": contact, "City": city}
        donors_db.append(donor_data)
        st.success(f"Donor {name} registered successfully!")

# View Donors Section
elif choice == "View Donors":
    st.title("Donor List")
    if donors_db:
        df = pd.DataFrame(donors_db)
        st.dataframe(df)
    else:
        st.warning("No donors registered yet.")

# Search Donor Section
elif choice == "Search Donor":
    st.title("Search for Donor")
    blood_type_search = st.selectbox("Select Blood Type to Search", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    if st.button("Search"):
        search_results = [donor for donor in donors_db if donor['Blood Type'] == blood_type_search]
        if search_results:
            st.write(f"Donors with Blood Type {blood_type_search}:")
            df = pd.DataFrame(search_results)
            st.dataframe(df)
        else:
            st.warning(f"No donors found with blood type {blood_type_search}.")
