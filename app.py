import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv 
load_dotenv() #activate api key
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

#Movie recommendation system
st.title(" ✨ Movie Recommendation System ✨")
user_input = st.text_input("Enter a movie you like:")
submit= st.button("Click here..")    
# if submit:
#     st.markdown("### Recommended Movies:")
# else:
#     st.warning("Please enter a movie name and click the button.")
model=genai.GenerativeModel('gemini-2.5-flash-lite')
if submit and user_input.strip():
    st.markdown(f'Movie name entered: {user_input}')
    response = model.generate_content(f"Generate Movie Recommendations based on this movie: {user_input}")
    st.write(f"Related Movie Recommendations: \n {response.text}")
else:
    st.write("No movie name entered yet.")