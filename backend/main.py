from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from pydantic import BaseModel
from memory import ChatMemory
from agent import run_agent

app = FastAPI()
memory = ChatMemory()

class Query(BaseModel):
    message: str

@app.post("/chat")
def chat(data: Query):

    context = memory.get_context()

    full_query = context + "\nUser: " + data.message

    # Run agent
    response = run_agent(full_query)

    memory.add(data.message, response)

    return {"reply": response}