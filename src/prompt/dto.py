from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class PromptRequestSchema(BaseModel):

    prompt: str

class PromptResponseSchema(BaseModel):
    id: UUID
    prompt: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
    
    