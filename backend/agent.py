
from langgraph.prebuilt import create_react_agent
from tools import weather_tool, news_tool, calculator_tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os

llm = ChatOpenAI(
    model="gpt-4.1",
    api_key=os.getenv("OPENAI_API_KEY")
)
tools = [
    {"name": "Weather", "func": weather_tool, "description": "Get weather info"},
    {"name": "News", "func": news_tool, "description": "Get latest news"},
    {"name": "Calculator", "func": calculator_tool, "description": "Do math"}
]

agent = create_react_agent(llm, tools)

def run_agent(query):
    response = agent.invoke({"messages": [("user", query)]})
    return response["messages"][-1].content