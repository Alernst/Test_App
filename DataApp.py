import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os


#@st.cache(allow_output_mutation=True)  
def authentication():
    name_c = st.secrets["DB_TOKEN"]
    username_c = st.secrets["DB_USERNAME"]
    password_c = st.secrets["DB_PASSWORD"]
    authentication_status = None
    
    with st.form(key="Login"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        st.form_submit_button("Login")
        if (username == username_c) & (password == password_c): 
            authentication_status = True
            st.write("Login successful")
        elif (username == "") | (password == ""):
            st.write("Enter a username and password")
        else:
            authentication_status = False
            st.write("Username/Password wrong")
    return (authentication_status, username)

st.title("CoVasc Drug Screening")
st.header("Login to see content (Click on sidebar)")
#name, authentication_status, username = authentication()
with st.sidebar:
    a_state,user = authentication()

if a_state:
    path = "Data/Example.xlsx"
    st.text(path)
    data = pd.read_excel(path)
    fig = px.violin(data)
    st.plotly_chart(fig,use_container_width=True)






#import pydeck as pdk
#import numpy as np#Load and Cache the data
#from skimage.io import imread, imshow 
#from PIL import Image
#from glob import glob
    
