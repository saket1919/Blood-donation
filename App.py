import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="सामना ढोल ताशा पथक लातूर", layout="wide")

# Custom CSS for UI
st.markdown("""
    <style>
        .main-header {
            background-color: #E50914;
            color: white;
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .section {
            background-color: #ffffff;
            border: 1px solid #dcdcdc;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
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
            background-color: #c40811;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="main-header">
        <h1>सामना ढोल ताशा पथक लातूर</h1>
    </div>
""", unsafe_allow_html=True)

# Database Setup
conn = sqlite3.connect('donors.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute("""
CREATE TABLE IF NOT EXISTS donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    blood_group TEXT NOT NULL,
    contact TEXT NOT NULL,
    state TEXT NOT NULL,
    city TEXT NOT NULL
)
""")
conn.commit()

# State and City Mapping
state_city_mapping = {"Maharashtra": [
        "Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Solapur", "Kolhapur",
        "Thane", "Amravati", "Sangli", "Jalgaon", "Nanded", "Akola", "Latur",
        "Dhule", "Ahmednagar", "Chandrapur", "Parbhani", "Beed", "Ratnagiri",
        "Gondia", "Wardha", "Satara", "Bhandara", "Yavatmal", "Raigad", "Palghar"
    ],
    "Karnataka": [
        "Bangalore", "Mysore", "Mangalore", "Hubli", "Belgaum", "Davanagere",
        "Bellary", "Shimoga", "Tumkur", "Bijapur", "Gulbarga", "Raichur", "Hassan"
    ],
    "Gujarat": [
        "Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar",
        "Junagadh", "Gandhinagar", "Anand", "Navsari", "Mehsana", "Morbi",
        "Surendranagar", "Amreli", "Palanpur"
    ],
    "Rajasthan": [
        "Jaipur", "Udaipur", "Jodhpur", "Kota", "Ajmer", "Bikaner", "Alwar",
        "Bharatpur", "Sikar", "Pali", "Tonk", "Barmer", "Jhunjhunu", "Churu"
    ],
    "Tamil Nadu": [
        "Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tirunelveli",
        "Erode", "Vellore", "Thoothukudi", "Dindigul", "Thanjavur", "Cuddalore",
        "Kanchipuram", "Nagercoil", "Karur"
    ]

}

# Sidebar for Options
st.sidebar.header("Select an Option")
option = st.sidebar.radio("Choose Action", ["Register as a Donor", "Search for Donors", "Data Insights"])

# Register as a Donor
if option == "Register as a Donor":
    st.subheader("Register as a Donor")
    name = st.text_input("Full Name")
    blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])

    # State and City Dynamic Selection
    state = st.selectbox("Select State", list(state_city_mapping.keys()))
    if state:
        city = st.selectbox("Select City", state_city_mapping[state])  # Dynamically update cities
    else:
        city = st.selectbox("Select City", ["Please select a state first"])  # Default option if no state selected
    
    contact = st.text_input("Contact Number")
    submitted = st.button("Register")
    if submitted:
        if name and blood_group and city and state and contact:
            c.execute("INSERT INTO donors (name, blood_group, contact, state, city) VALUES (?, ?, ?, ?, ?)",
                      (name, blood_group, contact, state, city))
            conn.commit()
            st.success("Donor Registered Successfully!")
        else:
            st.error("All fields are required!")



# Search for Donors
if option == "Search for Donors":
    st.subheader("Search for Donors")
    state_filter = st.selectbox("Select State", list(state_city_mapping.keys()))
    if state_filter:
        city_filter = st.selectbox("Select City", state_city_mapping[state_filter])  # Dynamically update cities
    else:
        city_filter = st.selectbox("Select City", ["Please select a state first"])  # Default option if no state selected
    
    blood_group_filter = st.selectbox("Select Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    if st.button("Search"):
        query = """
        SELECT name, blood_group, contact, city, state 
        FROM donors 
        WHERE state = ? AND city = ? AND blood_group = ?
        """
        c.execute(query, (state_filter, city_filter, blood_group_filter))
        results = c.fetchall()
        if results:
            df_results = pd.DataFrame(results, columns=["Name", "Blood Group", "Contact", "City", "State"])
            st.dataframe(df_results, use_container_width=True)
        else:
            st.info("No donors found for the selected criteria.")

# Data Insights
if option == "Data Insights":
    st.subheader("Data Insights")
    
    # Fetch Data for City and Blood Group Distribution
    c.execute("SELECT city, blood_group, COUNT(*) as count FROM donors GROUP BY city, blood_group")
    city_blood_group_data = pd.DataFrame(c.fetchall(), columns=["City", "Blood Group", "Count"])
    
    # Fetch Data for Blood Group Distribution
    c.execute("SELECT blood_group, COUNT(*) as count FROM donors GROUP BY blood_group")
    blood_group_data = pd.DataFrame(c.fetchall(), columns=["Blood Group", "Count"])
    
    # Combined Stacked Bar Chart with Line Chart
    st.write("### City and Blood Group Distribution (Stacked with Line)")
    
    if not city_blood_group_data.empty:
        # Calculate total counts per city for the line chart
        city_total_counts = city_blood_group_data.groupby("City")["Count"].sum().reset_index()

        # Create stacked bar chart
        fig = px.bar(
            city_blood_group_data,
            x="City",
            y="Count",
            color="Blood Group",
            title="City and Blood Group Distribution (Stacked with Line)",
            labels={"Count": "Donor Count"},
            text_auto=True
        )
        
        # Add line chart for total counts
        fig.add_scatter(
            x=city_total_counts["City"],
            y=city_total_counts["Count"],
            mode="lines+markers",
            name="Total Donor Count",
            line=dict(color='black', width=2)
        )
        
        # Customize layout
        fig.update_layout(
            xaxis_title="City",
            yaxis_title="Donor Count",
            legend_title="Blood Group",
            template="plotly_white",
            bargap=0.3  # Adjust bar spacing
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available for city and blood group distribution.")
    
    # Blood Group Pie Chart with Count Displayed
    st.write("### Blood Group Distribution (with Counts)")

    if not blood_group_data.empty:
        pie_chart = px.pie(
            blood_group_data,
            names="Blood Group",
            values="Count",
            title="Blood Group Distribution",
            hole=0.3,  # To create a donut chart, optional
            labels={"Count": "Donor Count"}
        )

        # Add count values directly to the chart
        pie_chart.update_traces(
            textinfo="label+value",  # Display labels and counts
            textfont_size=14,
            marker=dict(line=dict(color="#000000", width=1))  # Optional: outline
        )

        st.plotly_chart(pie_chart, use_container_width=True)
    else:
        st.info("No data available for blood group distribution.")

st.write("""
    **Note**: For issues or feedback, please contact the admin.
""")
