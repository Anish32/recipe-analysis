import streamlit as st
import pandas as pd
import pickle

# Load the saved model
model = pickle.load(open('/content/Rndm_rgsr_mdl.pkl', 'rb'))

# Streamlit app
st.title("Recipe Popularity Prediction")

Cooking_Time_Minutes = st.number_input("Enter Cooking Time in Minutes:", min_value=0.0)
Serving_Size = st.number_input("Enter Serving Size:", min_value=0.0)
Calories_Per_Serving = st.number_input("Enter Calories Per Serving:", min_value=0.0)
Cost_Per_Serving = st.number_input("Enter Cost Per Serving:", min_value=0.0)
Num_Ingredients = st.number_input("Enter Number of Ingredients:", min_value=0.0)

if st.button("Predict"):
    user_input = pd.DataFrame({
        'Cooking_Time_Minutes': [Cooking_Time_Minutes],
        'Serving_Size': [Serving_Size],
        'Calories_Per_Serving': [Calories_Per_Serving],
        'Cost_Per_Serving': [Cost_Per_Serving],
        'Num_Ingredients': [Num_Ingredients]
    })
    prediction = model.predict(user_input)
    st.success(f"The predicted popularity score is: {prediction[0]:.2f}")
