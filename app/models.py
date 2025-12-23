
from sqlalchemy import Column, Integer, String, DateTime
from app.db import Base

class ChatEntry(Base):
    __tablename__ = "chat_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_message = Column(String)
    assistant_message = Column(String)
    timestamp = Column(DateTime)
