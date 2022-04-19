from datetime import datetime
from typing import Optional, List
from xml.etree.ElementTree import Comment

import sqlalchemy
from pydantic import BaseModel, Field

metadata = sqlalchemy.MedtaData()

class CommentBase(BaseModel):
    post_id: int
    publication_date: datetime = Field(default_factory=datetime.now)
    content: str

class CommentCreate(CommentBase):
    pass

class CommentDB(CommentBase):
    id: int

class PostBase(BaseModel):
    title: str
    contetn: str
    publication_date: datetime = Field(default_factory=datetime.now)

class PostPartialUpdate(BaseModel):
    title: Optional[str] = None
    contetn: Optional[str] = None

class PostCreate(PostBase):
    pass

class PostDB(PostBase):
    id: int

class PostPublic(PostDB):
    comments: List[CommentDB]

posts = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("publictaion_date", sqlalchemy.DateTime(), nullable=False),
    sqlalchemy.Column("title", sqlalchemy.String(length=255), nullable=False),
    sqlalchemy.Column("content", sqlalchemy.Text(), nullable=False)
)

comments = sqlalchemy.Table(
    "comments",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("post_id", sqlalchemy.ForeignKey("post_id", ondelete="CASCADE"), nullable=False),
    sqlalchemy.Column("publication_date", sqlalchemy.DateTime(), nullable=False),
    sqlalchemy.Column("content", sqlalchemy.Text(), nullable=False),
)