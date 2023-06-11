import streamlit as st
import requests
from urllib.parse import parse_qs






# Parse the URL to get the parameters
params = st.experimental_get_query_params()



# Check if the user token exists in the URL
token = params.get('token', [None])[0]

# Set page layout
st.set_page_config(page_title="Construction Layout Confirmation", layout="wide")

hide_st_style ="""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
</style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)


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
st.markdown("Hello,")

st.markdown("Please view your final layout here.") # Add your markdown here

st.markdown(
    """
    <style>
    .rounded-button {
        display: inline-block;
        padding: 10px 20px;
        border-radius: 50px;
        background-color: #0080ff;
        color: white;
        font-size: 20px;
        text-decoration: none;
        text-align: center;
        cursor: pointer;
        border: none;
    }

    .rounded-button:hover {
        background-color: #005cb3;
    }
    </style>

    <div style="text-align: center;">
        <a href="your_download_link" target="_blank" class="rounded-button">Download plans</a>
    </div>
    """,
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns([2, 1, 2])

with col2:
    with st.container():
        st.write("")  # Add an empty placeholder to reserve space for the button
        approve_button = st.button("Approve")

col4, col5, col6 = st.columns([2, 1, 2])

with col5:
    with st.container():
        st.write("")  # Add an empty placeholder to reserve space for the button
        deny_button = st.button("Deny")






# Footer
st.markdown(
    """
    Thank you for choosing Voltaic.

    Sincerely,

    Voltaic Construction

    """
)
