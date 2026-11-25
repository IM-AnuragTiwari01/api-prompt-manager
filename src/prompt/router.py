from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.prompt.dto import PromptRequestSchema, PromptResponseSchema
from src.prompt import controller


prompt_route = APIRouter(prefix="/prompt")

@prompt_route.post("/upload-prompt", response_model=PromptResponseSchema)
def upload_prompt(body: PromptRequestSchema, db: Session = Depends(get_db)):
    return controller.upload_prompt(body, db)

@prompt_route.get("/all-prompts", response_model=List[PromptResponseSchema])
def all_prompts(db: Session = Depends(get_db)):
    return controller.all_prompts(db)

@prompt_route.get("/get-prompt/{prompt_id}", response_model=PromptResponseSchema)
def get_prompt(prompt_id: str, db: Session = Depends(get_db)):
    return controller.get_prompt(prompt_id, db)


