from typing import Optional
from fastapi import FastAPI, Header, Cookie

app = FastAPI()

@app.get('/')
async def get_header(hello: str = Header(...)):
    return {"hello": hello}

@app.get('/1')
async def get_header2(user_agent: str = Header(...)):
    return {"user_agent": user_agent}

@app.get('/2')
async def get_cookie(hello: Optional[str] = Cookie(None)):
    return {"hello": hello}