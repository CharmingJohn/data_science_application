from fastapi import FastAPI, Query
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

@app.get('/users3')
async def get_user3(page: int = Query(1, gt=0), size : int = Query(10, le=100)):
    return {"page": page, "size": size}