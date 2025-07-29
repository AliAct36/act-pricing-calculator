
import streamlit as st

# Pricing data
pricing = {'Standard': {'Annual': 300.0, 'Monthly': 33.33, 'Enhanced Support': 96.0, 'Custom Industry Tables': 96.0}, 'Professional': {'Annual': 450.0, 'Monthly': 50.0, 'Enhanced Support': 48.0, 'Custom Industry Tables': 48.0}, 'Ultimate': {'Annual': 600.0, 'Monthly': 66.67, 'Enhanced Support': 0.0, 'Custom Industry Tables': 0.0}}

st.title("Act! Advantage Pricing Calculator")

plan = st.selectbox("Select Plan", ["Standard", "Professional", "Ultimate"])
billing = st.radio("Billing Type", ["Annual", "Monthly"])
users = st.number_input("Number of Users", min_value=1, step=1)
enhanced_support = st.checkbox("Enhanced Support")
custom_tables = st.checkbox("Custom Industry Tables")

base_price = pricing[plan][billing] * users
support_price = pricing[plan]["Enhanced Support"] * users if enhanced_support else 0
tables_price = pricing[plan]["Custom Industry Tables"] * users if custom_tables else 0

total = base_price + support_price + tables_price

st.markdown(f"### Total Price: £{total:.2f} per year")
