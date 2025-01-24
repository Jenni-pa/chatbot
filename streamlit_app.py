import streamlit as st
import pydeck
import pandas as pd
import streamlit.components.v1 as components
from streamlit import session_state as ss

st.title("Find companies you are looking for")

# map stuff

st.markdown("Do you want to add a company?")
with st.popover("📎",use_container_width=True):
            #file upload:
            uploaded_file = st.file_uploader("Choose a file",type=['txt'])
            NameOfCmpny = st.text_input('Company name:')
            if st.button("add company"):
                st.write("Company added successfully")