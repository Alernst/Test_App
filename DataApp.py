import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os

with st.form("Login"):
    
    user = st.text_input("Username")
    pw = st.text_input("Password")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Login")
    if submitted:
        if (user == st.secrets["DB_USERNAME"]) & (pw == st.secrets["DB_PASSWORD"]): 
            success = True
            st.write("Logged in")
        else:
            success = False
            st.write("Login failed")
    success = False

    if success:

    #import pydeck as pdk
    #import numpy as np#Load and Cache the data
    #from skimage.io import imread, imshow 
    #from PIL import Image
    #from glob import glob
        path = "Data/Example.xlsx"
        st.text(path)
        data = pd.read_excel(path)
        fig = px.violin(data)
        st.plotly_chart(fig,use_container_width=True)
        st.plotly_chart(fig,use_container_width=True)
    