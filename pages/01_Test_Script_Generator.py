import streamlit as st
import pandas as pd

st.title("Create your Test Script here..!!")
st.caption("Below is the same test script for a demo, you can double-click on the cells to edit.")

df = pd.DataFrame(
    [
       {"Test Action": "Launch", "Locator": "n/a", "Test Data": "Chrome"},
       {"Test Action": "Navigate", "Locator": "n/a", "Test Data": "https://www.saucedemo.com/"},
       {"Test Action": "Input", "Locator": "//input[@id='user-name']", "Test Data": "standard_user"},
       {"Test Action": "Input", "Locator": "//input[@id='password']", "Test Data": "secret_sauce"},
       {"Test Action": "Click", "Locator": "//input[@id='login-button']", "Test Data": "n/a"},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

