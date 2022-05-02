import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import pydeck as pdk
import numpy as np#Load and Cache the data
from skimage.io import imread, imshow 
from PIL import Image
from glob import glob

data = pd.read_excel("C:/Users/aernst/Documents/GitHub/Test_App/Data/Example.xlsx")
fig = px.violin(data)
st.plotly_chart(fig,use_container_width=True)