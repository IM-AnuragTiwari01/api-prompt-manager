from fastapi import FastAPI
from src.utils.db import Base, engine
from src.users.router import user_route
from src.prompt.router import prompt_route

Base.metadata.create_all(engine) # as soon as our server starts it connects to db

app = FastAPI(title="Document Summarizer Agent")

app.include_router(user_route)
app.include_router(prompt_route)