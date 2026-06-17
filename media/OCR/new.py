import google.generativeai as genai
from new import api
genai.configure(api_key="AIzaSyArMQ-CSGifzYz8ej08sPLbfn7y-CJ-Pdk")
model=genai.GenerativeModel("gemini-1.5-pro")
print(model.generate_content("python").text)