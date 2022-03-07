from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError

class User(BaseModel):
    email: EmailStr
    website: HttpUrl

# Invalid email
try:
    User(email="jdoe", website="https://www.example.com")
except ValidationError as e:
     print(str(e))

# Invalid URL
try:
    User(email="jdoe@example.com", website="jdoe")
except ValidationError as e:
    print(str(e))