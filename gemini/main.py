import streamlit as sns
import google.generativeai as genai
from PIL import Image
from apikeyfile import api_key

genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-1.5-pro")
if "chat" not in sns.session_state:
    sns.session_state['chat']=model.start_chat(history=[])
sns.title("Chatbot")
user_input=sns.text_input("enter yor message: ")
file=sns.file_uploader("Upload an image",type=["jpg","png","jpeg"])
button=sns.button("send message")
if user_input and file and button:
    img=Image.open(file)
    response=model.generate_content([user_input,img]).text
    sns.wrte(response)
elif user_input and button:
    response=sns.session_state['chat'].send_message(user_input).text
    sns.session_state['history'].append(user_input,response)
    sns.write(response)
elif button:
    sns.error("No input text detected")
history=sns.button("view history")
if history:
    if sns.session_state['history']:
        for i,j in sns.session_state['history']:
            sns.write(f"user: {i}")
            sns.write(f"Bot: {j}")
    else:
        print("No history")
clear=sns.button("clear history")
if clear:
    if sns.session_state['history']:
        sns.session_state['chat']=model.start_chat(history=[])
        sns.session_state['history'].clear()
        sns.success("History Cleared successfully")