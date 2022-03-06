from fastapi import FastAPI, status, Response
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse
import os

app = FastAPI()

@app.get('/html', response_class=HTMLResponse)
async def get_html():
    return """
        <html>
            <head>
                <title>Hello world!</title>
            </head>
            <body>
                <h1>Hello world!</h1>
            </body>
        </html>
    """

@app.get('/text', response_class=PlainTextResponse)
async def text():
    return "Hello world!"

@app.get('/redirect')
async def redirect():
    return RedirectResponse('/new-url', status_code=status.HTTP_301_MOVED_PERMANENTLY)

@app.get('/cat')
async def get_cat():
    root_directory = os.path.dirname(path.dirname(__file__))
    picture_path = os.path.join(root_directory, 'assets', 'cat.jpg')
    return FileResponse(picture_path)

@app.get('/xml')
async def get_xml():
    content = """<?xml version="1.0" encoding="UTF-8"?>
        <Hello>World</Hello>
    """
    return Response(content=content, media_type="appliation/xml")