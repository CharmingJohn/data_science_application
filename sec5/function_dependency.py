from fastapi import FastAPI, Depends, HTTPException, Header, Query, status
from typing import Optional, Tuple

app = FastAPI()

async def pagination(skip: int = Query(0, ge=0), limit: int = Query(10, ge=0),) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)

@app.get('/items')
async def list_items(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}

@app.get('/things')
async def list_things(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}

def secret_header(secret_header: Optional[str] = Header(None)) -> None:
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)

@app.get('/protected-route', dependencies=[Depends(secret_header)])
async def protected_route():
    return {"hello": "world"}