from datetime import datetime
from sqlmodel import  Session, select
from models import Card

# Create


def create_card(session: Session, card: Card):
    session.add(card)
    session.commit()
    session.refresh(card)
    return card


# Read


def get_card(session: Session, card_id: int):
    card = session.get(Card, card_id)
    if card is None:
        return {"error": "Card not found"}
    return card


# Update


def update_card(session, card_id: int, title: str = None, content: str = None, priority: int = None) -> Card:
    card = session.get(Card, card_id)
    if card:
        if title is not None:
            card.title = title
        if content is not None:
            card.content = content
        if priority is not None:
            card.priority = priority
        card.update()
        session.commit()
        session.refresh(card)
    return card


# Delete


def delete_card(session, card_id: int) -> bool:
    card = session.get(Card, card_id)
    if card:
        session.delete(card)
        session.commit()
        return True
    return False
