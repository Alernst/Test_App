import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os
import streamlit_authenticator as stauth

@st.cache()
def authentication():
    names = [st.secrets["DB_TOKEN"],"Alex"]
    usernames = [st.secrets["DB_USERNAME"],"AE"]
    passwords = [st.secrets["DB_PASSWORD"],"230989"]

    authenticator = stauth.Authenticate(names,usernames,passwords,
                    'Show','me12',cookie_expiry_days=30)
    name, authentication_status, username = authenticator.login('Login','main')
    return (name, authentication_status, username)

    
def show_graph(name,authentication_status):
    st.write("Me")
    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.write('Welcome *%s*' % (name))
        st.title('Best results ever')
        path = "Data/Example.xlsx"
        st.text(path)
        data = pd.read_excel(path)
        fig = px.violin(data)
        st.plotly_chart(fig,use_container_width=True)
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')
        
name, authentication_status, username = authentication()


st.write(username)
button = st.button("Show")    

if button:
   show_graph(name,authentication_status)



#import pydeck as pdk
#import numpy as np#Load and Cache the data
#from skimage.io import imread, imshow 
#from PIL import Image
#from glob import glob
    
