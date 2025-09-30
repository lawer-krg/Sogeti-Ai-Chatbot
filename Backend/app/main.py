from fastapi import FastAPI
from pydantic import BaseModel
from chatbot_nlp import NLPChatbot  # Note the updated import!

app = FastAPI()
bot = NLPChatbot()

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(msg: Message):
    result = bot.chat(msg.message)
    return result

@app.get("/")
async def root():
    return {"message": "Sogeti AI Chatbot API is running with NLP!"}