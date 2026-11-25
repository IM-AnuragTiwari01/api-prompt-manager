from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.prompt.dto import PromptRequestSchema
from src.prompt.model import Prompts_DocSummary
from fastapi import HTTPException


def upload_prompt(body: PromptRequestSchema, db: Session):
    body_dict = body.model_dump()
    new_prompt = Prompts_DocSummary(**body_dict)

    db.add(new_prompt)
    db.commit()
    db.refresh(new_prompt)

    return new_prompt

def all_prompts(db: Session):
    prompts = db.query(Prompts_DocSummary).all()
    return prompts

def get_prompt(prompt_id: str, db: Session):
    prompt = db.query(Prompts_DocSummary).filter(Prompts_DocSummary.id == prompt_id).first()

    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")

    return prompt