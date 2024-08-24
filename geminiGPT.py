import os
import google.generativeai as genai
import streamlit as st
os.environ['GOOGLE_API_KEY']='AIzaSyDQIKg2wzDEAJtIHbABZNa3qaqcmvTz6PY'
#configure
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
model =genai.GenerativeModel('gemini-1.5-pro')

def generate(input_text):
    response = model.generate_content(input_text)
    return response.text

st.title('Gemini gpt')
input_text = st.text_input('write a prompt')
if input_text:
    st.write(generate(input_text))
