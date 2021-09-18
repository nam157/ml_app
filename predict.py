import streamlit as st
import pickle
import numpy as np




def loadmodel():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data



data = loadmodel()

regressor_loaded = data["model"]
le_country = data["le_country"]

def show_predict():
    st.title("Dự đoán lương Software Developer")
    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )
    
    con = st.selectbox("Country",countries)
    year = st.slider("Year experience",0,50,3)

    ok = st.button("Tính toán lương")
    if ok:
        X = np.array([[con,year]])
        X[:,0] = le_country.transform(X[:,0])
        X = X.astype(float)
        salary = regressor_loaded.predict(X)

        st.subheader(f"The estimated salary is ${salary[0]:.2f}")

