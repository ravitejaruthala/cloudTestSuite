import streamlit as st
import pandas as pd
from testFunctions import *

uploaded_file = st.file_uploader("**Upload a CSV file here**", type=["csv"])

if uploaded_file is not None:
    if uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(df)
        test_run = st.button("Run the test script")
        if(test_run):
            for _, row in df.iterrows():
                if row[0].lower() == "click":
                    click(row[1].lower())
                elif row[0].lower() == "close":
                    close_browser()
                elif row[0].lower() == "input":
                    send_keys(row[1].lower(), row[2].lower())
                elif row[0].lower() == "launch":
                    launch_browser(row[2].lower())
                elif row[0].lower() == "navigate":
                    navigate_to_page(row[2].lower())
                    
    else:
        st.warning("Unsupported file type.")
