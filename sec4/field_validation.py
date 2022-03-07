from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, ValidationError, EmailStr, HttpUrl

class Person(BaseModel):
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    age: Optional[int] = Field(None, ge=0, le=120)

def list_factory():
    return ['a','b','c']

class Model(BaseModel):
    l : List[str] = Field(default_factory=list_factory)
    d: datetime = Field(default_factory=datetime.noew)
    l2: List[str] = Field(default_factory=list)

class User(BaseModel):
    email: EmailStr
    website: HttpUrl

# Invalid email
try:
    User(email="jdoe", website="https://www.example.com")
except ValidationError as e:
    print(str(e))

# Invalid URL
try:
    User(email="jdoe@example.com", website="jdoe")
except ValidationError as e:
    print(str(e))