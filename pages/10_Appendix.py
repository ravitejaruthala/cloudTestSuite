import streamlit as st

appendix_data = '''
**Close** : To close the browser \n
**Click** : To perform a click action on a web element \n
**Input** : To send input values to the webelements on the application under test \n
**Launch** : To launch a specific browser. User have options like Chrome, FireFox, MS Edge, Safari \n
**Navigate** : To navigate to a specfic website. It takes test data for the URL \n
'''

st.markdown(appendix_data)