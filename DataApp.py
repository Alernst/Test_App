import streamlit as st
import pandas as pd
import plotly.express as px
import os



st.title("Demo App")


path = "Data/Example.xlsx"
data = pd.read_excel(path)

options = st.multiselect(
     'What are your favorite colors',
     data.columns,
     data.columns[:2])


points = st.checkbox('Show points')


if points:
    fig = px.violin(data[options], points="all")

else:
    fig = px.violin(data[options])
    
st.plotly_chart(fig,use_container_width=True)



