import gradio as gr
import pandas as pd
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from langchain_core.prompts import PromptTemplate
from langchain_community.agent_toolkits import create_sql_agent
import os 
agent=None
def agent_prompt():
  prompt_template = PromptTemplate(
    input_variables=["input", "top_k","agent_scratchpad"],
    template="""
You are an AI-powered investor assistant. Your goal is to match investors with startups based on custom investor filters. Investors may filter based on one or more preferences (e.g., industry, funding range, startup stage, traction). Your task is to find the best-matching startups, rank them, and provide a match score (0-100).

### **Investor Preferences:**  
The investor has provided the following filters:  
- **Preferred Industry:**  *(if provided)*  
- **Investment Range:**  *(if provided)*  
- **Preferred Startup Stage:** *(if provided)*  
- **Minimum Traction Requirement:**  *(if provided)*  
### **Task:**  
1. **Filter startups** based on the investor's provided preferences.  
   - If an investor provides multiple filters, prioritize startups that match all or most criteria.  
   - If an investor provides only one filter (e.g., just industry), rank startups primarily on that criterion.  
2. **Calculate how strong the investor preferences are matching to each startup (0-100)**   
3. **Rank startups from highest to lowest match** and provide reasoning. 
4. **Provide the output in a structured format**.  

### Input: {input}
### Top K: {top_k}
###agent_scratchpad:{agent_scratchpad}
###Output format should be structured which is in normal format
"""
)
  return prompt_template

def pre_launch_operations():
  global agent
  df=pd.read_json('/content/Combined file.xlsx - Sheet1.json')
  db_filename = "titanic.db"
  if os.path.exists(db_filename):
    os.remove(db_filename)
  llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key="AIzaSyC6TmVb5Vk5J0r6z0oCmjvNgzbblDKuf3Y",
    handle_parsing_errors=True)
  engine = create_engine(f"sqlite:///{db_filename}")
  try:
    df.to_sql("startups", engine, index=False, if_exists="replace")
  except:
    pass
  prompt=agent_prompt()
  db = SQLDatabase(engine=engine)
  agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True,prompt=prompt)
  agent=agent_executor
  

def chat_interface(message, history):
  global agent
  return agent.invoke({"input": message})['output']
pre_launch_operations() 
chatbot = gr.ChatInterface(chat_interface)
chatbot.launch()
