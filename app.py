from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv() #load all environment variables

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

#Set Page title and header
st.set_page_config(page_title="Nutrition Expert", page_icon= "😀😀😀😀")
st.header("Food Calories Calculator Web Application")

# ask user to upload image
userInput = st.text_input("Write your question here..", key="input")
uploaded_image = st.file_uploader("Choose an Image...", type=["jpeg", "jpg", "png"])
image = ""
submit_button = st.button("Submit")

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.write(image, caption="uploaded Image")

input_prompt = """
You are a nutrition expert where you need to see the food items present in the input image 
and then answer the question being asked. if the user don't ask any question, 
then calculate the total calories also provide the details of each food items with calorie intake in the following format:
1. Item 1 - No of calories
2. Item 2 - No of calories
--------------------------
--------------------------

Please don't answer any question which is not related to food, or uploaded image, simply say "I am not capable to answer this"
"""
if submit_button:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_prompt, image, userInput])
    st.write(response.text)