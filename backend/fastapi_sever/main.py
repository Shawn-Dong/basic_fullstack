from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import APIs

app = FastAPI(title="simple FastAPI demo")

app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"],
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)

class Message(BaseModel):
     id: int
     text: str

class MessageCreate(BaseModel):
     text: str

messages_db = [
     Message(id=1, text="Hello from fastAPI"),
     Message(id=2, text="This is a demo message")
]