from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

@app.post('/files')
async def upload_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post('/files2')
async def upload_file2(file: UploadFile = File(...)):
    return {"file_name": file.filename, "content_type": file.content_type}

@app.post('/files3')
async def uploade_file3(files: List[UploadFile] = File(...)):
    return [{"file_name": file.filename, "content_type": file.content_type} for file in files]