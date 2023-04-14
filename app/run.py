

from fastapi import FastAPI
from app.routers import matched_mismatched_words

app = FastAPI()
app.include_router(matched_mismatched_words.router)