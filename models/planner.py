import os
from dotenv import load_dotenv

# For LLM agent (LangChain or OpenAI-compatible)
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.prompts import PromptTemplate

load_dotenv()
API_KEY = os.getenv('GROQ_API_KEY') or os.getenv('OPENAI_API_KEY')

# Simple planner using LLM
def plan_analysis(schema_info):
    prompt = f"""
    You are an AutoData Analyst. Given this dataset schema:
    {schema_info}
    1. List the steps you would take to analyze and clean this data.
    2. Justify each step.
    3. Suggest what to visualize and what to clean.
    """
    llm = OpenAI(openai_api_key=API_KEY)
    response = llm(prompt)
    return response 