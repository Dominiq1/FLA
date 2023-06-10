import streamlit as st
import requests
from urllib.parse import parse_qs

# Parse the URL to get the parameters
params = st.experimental_get_query_params()

# Check if the user token exists in the URL
token = params.get('token', [None])[0]

# Set page layout
st.set_page_config(page_title="Construction Layout Confirmation", layout="wide")

# Company logo
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.image("voltaicLogo.png", width=200)

# Header
col4, col5, col6 = st.columns([1,6,1])
with col5:
    st.title("Final Layout Confirmation")

# Welcome message with token
if token:
    st.write(f"Welcome, {token}")

# Homeowner information
st.write("FLA: Homeowner")

# Confirmation letter content
st.markdown("...")  # Add your markdown here

# Download plans button
st.markdown(
    """
    <div style="text-align: center;">
        <a href="your_download_link" target="_blank">
            <button class="btn btn-success" style="color: white; font-size: 20px;">Download plans</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Buttons for approval and denial
col7, col8, col9 = st.columns([2,1,2])
with col8:
    if st.button("Approve"):
        # rest of your code here
        pass

col10, col11, col12 = st.columns([2,1,2])
with col11:
    if st.button("Deny"):
        # rest of your code here
        pass

# Footer
st.markdown(
    """
    Thank you for choosing Voltaic.

    Sincerely,

    Voltaic Construction

    """
)
