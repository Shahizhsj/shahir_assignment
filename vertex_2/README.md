# AI Startup Pitch Deck Evaluation Workflow

## Objective
Develop an AI model that evaluates startup pitch decks based on specific criteria and provides a structured score with detailed feedback.

## Workflow Steps

### 1. Import Required Libraries
First, import the necessary libraries for the project:
- `gradio` for building the web interface.
- `google.generativeai` for using Google's Generative AI Model.
- `time` for handling delays.
- `os` and `re` for file operations and regex.

### 2. Set Up API Key
Configure the Google Generative AI API key for accessing the model.

### 3. Define the File Upload Function
Create a function `file_upload` to handle file uploads. This function will:
- Extract the filename.
- Configure the Generative AI API.
- Upload the pitch deck file to the API.
- Wait for the file processing to complete.
- Define a prompt to evaluate the pitch deck based on specified criteria.
- Generate content using the AI model and return the response.

### 4. Set Up Gradio Interface
Use Gradio to create a user interface for uploading files:
- Create a file input component for users to upload their pitch decks.
- Create a text box to display the AI's evaluation and feedback.
- Link the file upload function to the file input component.

### 5. Launch the Interface
Launch the Gradio interface in debug mode to allow users to interact with the AI model and receive evaluations of their pitch decks.

### Conclusion
This workflow enables users to upload startup pitch decks and receive detailed evaluations based on clarity, market opportunity, business model, traction, competitive advantage, team, investment ask, and design.

### Web App : [Link](https://huggingface.co/spaces/shahir123/vertex_2)
