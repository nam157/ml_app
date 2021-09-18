import streamlit as st
import pickle
import numpy as np
from predict import show_predict
from explore_Data import show_explore

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))
if page == "Predict":
    show_predict()
else:
    show_explore()