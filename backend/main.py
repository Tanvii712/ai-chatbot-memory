from fastapi import FastAPI
from pydantic import BaseModel
from memory import ChatMemory
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()

# Debug check
print("Loaded API KEY = ", os.getenv("OPENAI_API_KEY"))

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()
memory = ChatMemory()


class Query(BaseModel):
    message: str


@app.post("/chat")
def chat(data: Query):

    # Build prompt with memory
    past = memory.get()
    prompt = f"Previous messages:\n{past}\n\nUser: {data.message}"

    # New OpenAI API format
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    reply = response.choices[0].message["content"]

    # Save new message into memory
    memory.add(data.message, reply)

    return {"reply": reply}