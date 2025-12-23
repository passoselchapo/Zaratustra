
from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from datetime import datetime
from pydantic import BaseModel

from app.db import Base, get_db, some_engine
from app.models import ChatEntry
from app.agent import call_llm_agent

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=some_engine)

class ChatMessage(BaseModel):
    user_message: str

@app.post("/chat")
async def chat(message: ChatMessage, db: Session = Depends(get_db)):
    user_message = message.user_message

    # Call the LLM agent
    assistant_message = call_llm_agent(user_message)

    # Save messages to the database
    chat_entry = ChatEntry(
        user_message=user_message,
        assistant_message=assistant_message,
        timestamp=datetime.now()
    )
    db.add(chat_entry)
    db.commit()
    db.refresh(chat_entry)

    return {"assistant_message": assistant_message}

