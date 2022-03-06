from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class Company(BaseModel):
    name: str

app = FastAPI()

@app.post('/users/')
async def create_user(name: str = Body(...), age: int=Body(...)):
    return {"name": name, "age": age}

@app.post('/users2/')
async def create_user2(user: User):
    return {"user": user}

@app.post('/users3/')
async def create_user3(user: User, company: Company):
    return {"user": user, "company": company}

@app.post('/users4/')
async def create_user4(user: User, priority: int = Body(..., ge=1, le=3)):
    return {"user": user, "priority": priority}