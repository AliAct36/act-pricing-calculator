
import streamlit as st

# Pricing data
pricing = {
    "Standard": {
        "Annual": {"base": 300, "support": 96, "tables": 96},
        "Monthly": {"base": 33.33, "support": 10.67, "tables": 10.67}
    },
    "Professional": {
        "Annual": {"base": 450, "support": 48, "tables": 48},
        "Monthly": {"base": 50.00, "support": 5.33, "tables": 5.33}
    },
    "Ultimate": {
        "Annual": {"base": 600, "support": 0, "tables": 0},
        "Monthly": {"base": 66.67, "support": 0, "tables": 0}
    }
}

# Streamlit UI
st.title("Act! Advantage Pricing Calculator (GBP May 2025)")

plan = st.selectbox("Select Plan", ["Standard", "Professional", "Ultimate"])
billing = st.radio("Billing Type", ["Annual", "Monthly"])
users = st.number_input("Number of Users", min_value=1, step=1, value=1)
enhanced_support = st.checkbox("Include Enhanced Support")
custom_tables = st.checkbox("Include Custom Industry Tables")

# Calculate total
base_price = pricing[plan][billing]["base"] * users
support_price = pricing[plan][billing]["support"] * users if enhanced_support else 0
tables_price = pricing[plan][billing]["tables"] * users if custom_tables else 0
total = base_price + support_price + tables_price

# Display result
st.markdown(f"### Total Price: £{total:.2f} ({billing} billing)")

# Breakdown
st.markdown("#### Price Breakdown")
st.write(f"Base Price ({users} user(s)): £{base_price:.2f}")
if enhanced_support:
    st.write(f"Enhanced Support: £{support_price:.2f}")
if custom_tables:
    st.write(f"Custom Industry Tables: £{tables_price:.2f}")
