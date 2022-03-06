from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
async def get_rquest_object(request: Request):
    return {"path": request.url.path}