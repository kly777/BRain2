from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from crub import create_card, get_card

from database import SessionDep
from database import create_db_and_tables
from models import Card
app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/card/{card_id}")
async def card(card_id: int, session: SessionDep):
    print(card_id)
    print(card_id)
    print(card_id)
    print("\n")
    return get_card(session,card_id)

@app.post("/card")
async def create_card_endpoint(session: SessionDep,card: Card):
    return create_card(session,card)
