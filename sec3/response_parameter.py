from fastapi import FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    nb_views: int

#setting headers

@app.get('/')
async def custom_header(response: Response):
    response.headers["Custom-Header"] = "Custom-Header-Value"
    return {"hello": "world"}

@app.get('/1')
async def custom_cookie(response: Response):
    response.set_cookie("cookie-name", "cookie-value", max_age=86400)
    return {"hello": "world"}

posts = {
    1: Post(title = 'Hello', nb_view=100),
}

@app.put('/posts/{id}')
async def update_or_create_post(id: int, post: Post, response: Response):
    if id not in posts:
        response.status_code = status.HTTP_201_CREATED
    posts[id] = post
    return posts[id]