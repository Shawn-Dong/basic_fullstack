from fastapi import FastAPI, HTTPException
from typing import List
from main import app, Message, MessageCreate, messages_db

@app.get("/")
async def root():
     return {"status": "ok", "message": "FastAPI server is running"}

@app.get("/api/messages", response_model=List[Message])
async def get_messages():
    return messages_db

@app.get("/api/messages/{message_id}", response_model=Message)
async def get_message(message_id: int):
     for message in messages_db:
          if message.id == message_id:
               return message
     raise HTTPException(status_code=404, detail=f"Message with id {message_id} not found")

@app.post("/api/messages", response_model=Message, status_code=201)
async def create_message(message: MessageCreate):
     new_id = max([m.id for m in messages_db], default=0) + 1
     new_message = Message(id=new_id, text=message.text)
     messages_db.append(new_message)
     return new_message

if __name__ == "__main__":
     uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)