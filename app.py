import streamlit as st
import google.generativeai as genai
from pathlib import Path

api_key="AIzaSyB06BULxPhpIFfbIz_rHSL75CweAM_FZzk"
genai.configure(api_key=api_key)
generation_config={
    "temperature":0.4,
    "top_p":1,
    "top_k":32,
    "max_output_tokens":4096
}
model = genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=generation_config)
prompt='''You are an expert agronomist AI assistant helping small-scale farmers identify and treat plant diseases. The user has uploaded an image of a crop showing signs of disease. Analyze the image and provide the following in simple terms:
Below 7 main topic  should be bold

Disease or Pest Detected (if any):
Clearly name the disease or pest affecting the plant.

Confidence Level:
Estimate how confident you are in this diagnosis (e.g., High, Medium, Low).

Description of the Problem:
Briefly explain the symptoms visible in the image (e.g., yellow spots, curled leaves, fungal patches).

Cause and Impact:
What causes this disease/pest and how it impacts plant health and yield.

Recommended Remedies:
List practical, affordable treatments available in Karnataka (e.g., neem-based pesticide, carbendazim, pruning). Include both organic and chemical options if possible.

Urgency Level:
State how urgent the treatment is (e.g., Immediate, Monitor, Not serious).

Prevention Tips:
Suggest simple, preventative measures to avoid recurrence.'''


st.set_page_config(page_title="Project Kissan",page_icon=":robot")

col1, col2, col3,col4,col5 = st.columns([1, 2,3,2, 1])
with col3:
    st.image("logo.png", width=200)

st.title("Project Kisan")

st.subheader("An application that empowers farmers with AI-driven crop diagnosis, market insights, and scheme guidance")

uploadedfile=st.file_uploader("Upload an image",type=["png","jpg","jpeg"])
if uploadedfile:
   st.image(uploadedfile,width=250)

submit=st.button("Generate analysis")

if submit:
    image=uploadedfile.getvalue()
    imageparts= {
            "mime_type": "image/jpeg",
            "data":image,
        }
    
    response = model.generate_content(
    [ imageparts
       ,
        prompt,
    ]
)
    st.title("Here is the analysis based on your image:")
    st.write(response.text)