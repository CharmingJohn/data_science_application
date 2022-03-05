from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/users/{id}')
async def get_user(id: int = Path(..., ge=1)):
    return {"id": id}

@app.get('license-plates/{license}')
async def get_license_plate(license: str = Path(..., min_length=9, max_length=9)):
    return {"license": license}

@app.get('license-plates-2/{license}')
async def get_license_plate_2(license: str = Path(..., regex=r"^\w{2}-\d{3}-\w{2}$")):
    return {"license": license}