from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class UserFormat(str, Enum):
    SHORT = 'short'
    FULL = 'full'

@app.get('/users')
async def get_user(page: int = 1, size: int = 10):
    return {"page": page, "size": size}

@app.get('/users2')
async def get_user2(format: UserFormat):
    return {"format": format}