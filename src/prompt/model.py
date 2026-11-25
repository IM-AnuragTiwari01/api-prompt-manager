from src.utils.db import Base
import uuid
from sqlalchemy import Column, UUID, DateTime, Text
from sqlalchemy.sql import func

class Prompts_DocSummary(Base):
    __tablename__ = "prompts_docsummary"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    prompt = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())