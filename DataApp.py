import streamlit as st
import pandas as pd
import plotly.express as px
import os
from PIL import Image


st.title("Demo App")


path = "Data/Example.xlsx"
data = pd.read_excel(path)

#options = st.multiselect(
#     'Which columns to show?',
#     data.columns)


#points = st.checkbox('Show points')

#im = Image.open("fish.png")
#st.image(im, caption='fish')

#if points:
#    fig = px.violin(data[options], points="all")

#else:
#    fig = px.violin(data[options])
fig = px.violin(data)

st.plotly_chart(fig,use_container_width=True)


