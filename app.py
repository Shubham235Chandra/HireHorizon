import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import json
from docx import Document
from dotenv import load_dotenv

load_dotenv()  # Load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(resume_text, jd):

    # Format the input prompt with the actual data
    formatted_prompt = input_prompt.format(text=resume_text, jd=jd)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(formatted_prompt)
    return response.text

def input_pdf_text(uploaded_file):

    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:  # Iterate over each page in the PDF
        text += page.extract_text() if page.extract_text() else ""  # Append the extracted text
    return text

def input_docx_text(uploaded_file):

    doc = Document(uploaded_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Prompt
input_prompt = """
Hey, act like an advanced ATS (Application Tracking System) with extensive expertise in the tech field, including software engineering, data science, data analytics, and big data engineering. 
Your main task is to evaluate the resume in comparison with the provided job one description. 
Given the highly competitive job market, your analysis should offer detailed assistance to improve the resume. 
Provide a score reflecting the percentage match between the resume and the job description, identify critical missing keywords, and offer a concise profile summary that could enhance the applicant's alignment with the job.

- Resume Text: {text}
- Job Description: {jd}

Response format:
{{
  "JD Match": "%",
  "Missing Keywords": [],
  "Profile Summary": ""
}}
"""

## Streamlit App
st.title("Hire Horizon")
st.text("Enhance Your Resume to Match Job Descriptions")


# Sidebar for inputs
with st.sidebar:
    jd = st.text_area("Paste the Job Description")
    uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf", "docx"], help="Please upload the PDF or DOCX of your resume")
    st.text("Please upload the PDF or DOCX of your Resume")
    submit = st.button("Submit")

if submit:

    if uploaded_file is not None and jd:

        if uploaded_file.type == "application/pdf":
            resume_text = input_pdf_text(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = input_docx_text(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a PDF or DOCX file")
            resume_text = None

        if resume_text:
            response = get_gemini_response(resume_text, jd)
            try:
                # Try to parse the JSON response
                response_data = json.loads(response)
                
                # Display each component separately
                st.subheader("Profile Summary")
                st.write(response_data['Profile Summary'] if response_data['Profile Summary'] else "No additional profile summary provided.")

                st.subheader("Job Description Match")
                st.write(f"{response_data['JD Match']} Match")
                
                st.subheader("Missing Keywords")
                if response_data['Missing Keywords']:
                    st.write(response_data['Missing Keywords'])
                else:
                    st.write("Resume Seems Perfect")
                
            except json.JSONDecodeError:
                st.error("Failed to decode the response. The response was not in valid JSON format. Please check the model output.")