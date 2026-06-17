import streamlit as st
import pytesseract
import re
import numpy as np
import cv2
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("Pattern Extractor Web App from Images")

# Regular expressions
email_pattern = re.compile(r"[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+")
phone_pattern = re.compile(r"\b\+?9?1?\d{10}\b")
website_pattern = re.compile(r"www\.[a-zA-Z0-9]+\.[a-zA-Z]+")

patterns = {"Email": email_pattern, "Phone Number": phone_pattern, "Website": website_pattern}

# File uploader
file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Dropdown for pattern selection
user_pattern = st.selectbox("Select pattern to extract", list(patterns.keys()))

# Function to extract patterns
def extract_patterns(img_array, pattern):
    text = pytesseract.image_to_string(img_array)
    return pattern.findall(text) if pattern.findall(text) else None

# Extract button
if file and user_pattern and st.button("Extract"):
    img = Image.open(file)
    img = np.array(img)

    # Convert to grayscale for better OCR
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 3)

    # Extract text
    selected_pattern = patterns[user_pattern]
    results = extract_patterns(gray, selected_pattern)

    if results:
        for match in results:
            st.write(match)
    else:
        st.write("No match found.")
