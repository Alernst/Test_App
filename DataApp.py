import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os
#import pydeck as pdk
#import numpy as np#Load and Cache the data
#from skimage.io import imread, imshow 
#from PIL import Image
#from glob import glob
"Data/Example"
path = "https://raw.githubusercontent.com/alernst/Test_App/Data/Example.xlsx"
st.text(path)
data = pd.read_excel(path)
fig = px.violin(data)
st.plotly_chart(fig,use_container_width=True)