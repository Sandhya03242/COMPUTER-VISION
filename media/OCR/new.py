import google.generativeai as genai
from new import api
genai.configure(api_key="")
model=genai.GenerativeModel("gemini-1.5-pro")
print(model.generate_content("python").text)
