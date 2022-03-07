from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import List
from fastapi import FastAPI, status

app = FastAPI()

class Gender(str, Enum):
    MALE= 'MALE'
    FEMALE= 'FEMALE'

class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str

class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]
    address: Address

person = Person(
    first_name="John",
    last_name="Doe",
    gender=Gender.MALE,
    birthdate="1991-01-01",
    interests=["travel", "sports"],
    address={
        "street_address": "12 Squirell Street",
        "postal_code": "424242",
        "city": "Woodtown",
        "country": "US",
        },
    )
person_dict = person.dict()
print(person_dict["first_name"]) # "John"
print(person_dict["address"]["street_address"]) # "12 SquirellStreet"

person_include = person.dict(include={"first_name", "last_name"})
print(person_include) # {"first_name": "John", "last_name":"Doe"}
person_exclude = person.dict(exclude={"birthdate","interests"})
print(person_exclude)

person_nested_include = person.dict(
    include={
        "first_name": ...,
        "last_name": ...,
        "address": {"city", "country"},
        }
    )
# {"first_name": "John", "last_name": "Doe", "address": {"city": "Woodtown", "country": "US"}}
print(person_nested_include)

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostPublic(PostBase):
    id: int

class PostDB(PostBase):
    id: int
    nb_views: int = 0

@app.post('/posts', status_code=status.HTTP_201_CREATED, response_model=PostPublic)
async def create(post_create: PostCreate): 
    new_id = max(db.posts.keys() or (0,)) + 1
    post = PostDB(id=new_id, **post_create.dict())
    db.posts[new_id] = post
    return post