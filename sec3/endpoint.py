from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class UserType(str, Enum):
    STANDARD = 'standard'
    ADMIN = 'admin'


@app.get('/')
async def hello_world():
    return {"hello": "world"}


@app.get('/users/{id}/')
async def get_user(id: int):
    return {"id": id}


@app.get('/users/{type}/{id}/')
async def get_user_2(type: type, id: int):
    return {"type": type, "id": id}


@app.get('/users/{type}/{id}/')
async def get_user_3(type: UserType, id: int):
    return {"type": type, "id": id}