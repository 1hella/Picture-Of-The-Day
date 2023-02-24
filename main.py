import os
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
if api_key is None:
    api_key = "DEMO_KEY"
    print("Using DEMO_KEY, put your own api_key in an .env file. ")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
content = response.json()

st.title(content['title'])

st.image(content['url'])

st.write(content['explanation'])