import streamlit as st
import numpy as np
import cv2
import re
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


email = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
phone = re.compile(r"(\+\d{1,3}[-\s]?\d{1,4}[-\s]?\d{3}[-\s]?\d{3,4})")
website = re.compile(r"www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

patterns={"Email":email,"Phone":phone,"Website links":website}

st.title("PATTERN EXTRACTOR WEBAPP FROM IMAGES")
file=st.file_uploader('Upload an image',type=['jpg','png','jpeg'])
user_pattern=st.selectbox('Select a pattern',patterns.keys())
button=st.button("Extract")

if file and user_pattern and button:
    img=Image.open(file)
    img=np.array(img)
    img=cv2.GaussianBlur(img,(3,3),2)

    text=pytesseract.image_to_string(img)
    patt=patterns[user_pattern]
    res=patt.findall(text)
    if res:
        for i in res:
            st.write(f"{i}\n")
    else:
        st.write("NO MATCH FOUND")