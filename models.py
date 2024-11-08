from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime


class Card(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    # created_time: datetime|None = Field()
    # update_time: datetime|None = Field()
    priority: int = Field(default=0)

    # relations: List["Relation"] = Relationship(back_populates="card")
    # tags: List["Tag"] = Relationship(back_populates="card")
    # todos: List["ToDo"] = Relationship(back_populates="card")
    # reviews: List["Review"] = Relationship(back_populates="card")

    def __str__(self):
        return self.title



# class Relation(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     relate_card_id: int = Field(foreign_key="card.id")
#     card_id: int = Field(foreign_key="card.id", default=None)
#     position: int = 0
#     priority: int = 0

#     card: Card = Relationship(back_populates="relations",link_model=Card)
#     relate_card: Card = Relationship(
#         back_populates="relations", link_model=Card)

#     class Config:
#         unique_together = ('card', 'position')


# class Tag(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     tag: int = Field(foreign_key="card.id")
#     card_id: int = Field(foreign_key="card.id")
#     priority: int = 0

#     card: Card = Relationship(back_populates="tags")

#     class Config:
#         unique_together = ('tag', 'card')

#     def __str__(self):
#         return self.tag.title


# class ToDo(SQLModel, table=True):
#     id:  int = Field(default=None, primary_key=True)
#     card_id: int = Field(foreign_key="Card.id")
#     state: int = 0
#     full_time: bool = False
#     start: Optional[datetime] = None
#     end: Optional[datetime] = None
#     priority: int = 0

#     card: Card = Relationship(back_populates="todos")

#     def __str__(self):
#         return self.card.title


# class Review(SQLModel, table=True):
#     id:  int = Field(default=None, primary_key=True)
#     card_id: int = Field(foreign_key="Card.id")
#     state: int = 0
#     time: Optional[datetime] = None

#     card: Card = Relationship(back_populates="reviews")

#     def __str__(self):
#         return self.card.title

#     class Config:
#         unique_together = ('card',)
