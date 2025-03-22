import gradio as gr
import google.generativeai as genai
import time
import os
import re  # Import regex module

prompt="""Task:
You are an AI model that evaluates startup pitch decks based on clarity, market opportunity, business model, traction, competitive advantage, team, investment ask, and design. Your goal is to analyze a pitch deck and provide a structured score (out of 100) with explanations for each category.

Input:

A startup’s pitch deck in PDF/PPT format or as extracted text.
The following evaluation criteria:
Clarity & Storytelling (15%) – Is the problem well-defined? Is the solution compelling?
Market Opportunity (15%) – Is the target market size realistic and well-researched?
Business Model & Revenue Strategy (15%) – How does the startup make money? Is the revenue model scalable?
Traction & Validation (15%) – Does the startup show real-world progress (customers, revenue, partnerships)?
Competitive Advantage (10%) – What makes this startup unique compared to competitors?
Team & Execution Capability (10%) – Does the team have the right experience to execute the vision?
Investment Ask & Fund Utilization (10%) – Is the funding request clear with a proper breakdown?
Design & Engagement (10%) – Is the presentation visually appealing and easy to understand?
Output:

A detailed score breakdown (out of 100).
Strengths and weaknesses in each category.
Personalized feedback

"""
GOOGLE_API_KEY = "AIzaSyC6TmVb5Vk5J0r6z0oCmjvNgzbblDKuf3Y"

def file_upload(file):
    file_name = "abcde"  # Extract filename without extension

    genai.configure(api_key=GOOGLE_API_KEY)

    try:
        pdfFile = genai.get_file(f"files/{file_name}")
    except:
        pdfFile = genai.upload_file(path=file.name, name=file_name, resumable=True)
    while pdfFile.state.name == "PROCESSING":
      time.sleep(10)
      pdfFile = genai.get_file(pdfFile.name)
    if pdfFile.state.name == "FAILED":
      raise ValueError(pdfFile.state.name)

    model = genai.GenerativeModel(
            model_name="models/gemini-2.0-flash",
            system_instruction=[prompt],  # Define prompt here
        )
    response = model.generate_content([pdfFile, prompt], request_options={"timeout": 600})
    return response.text

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            file_input = gr.File(label="Upload a file")
            file_output = gr.Textbox()
            file_input.upload(fn=file_upload, inputs=file_input, outputs=file_output)

demo.launch(debug=True)
