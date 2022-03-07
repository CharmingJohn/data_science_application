from datetime import date

from pydantic import BaseModel, validator, EmailStr, ValidationError, root_validator

class Person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

    @validator('birthdate')
    def valid_birthdate(cls, v: date):
        delta = date.today() - v
        age = delta.days/365
        if age > 120:
            raise ValueError('Yoo seem a bit too old!')
        return v

class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str

    @root_validator()
    def passwords_match(cls, values):
        password = values.get('password')
        password_confirmation = values.get('password_confirmation')
        if password != password_confirmation:
            raise ValueError('Passwords don\'t match')

        return values