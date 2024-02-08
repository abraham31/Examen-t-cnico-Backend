from typing import List
from pydantic import BaseModel

class Comment(BaseModel):
    comment: str
    rating: int

class Show(BaseModel):
    id: int
    name: str
    channel: str
    summary: str
    genres: List[str]
    comments: List[Comment] = []

class CommentInput(BaseModel):
    show_id: int
    comment: str
    rating: int