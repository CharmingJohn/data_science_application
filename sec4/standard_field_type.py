from datetime import date
from enum import Enum
from typing import List

from pydantic import BaseModel, ValidationError

class Gender(str, Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdata: date
    interests: List[str]
    

# invalid gender
try: Person(
    first_name='John',
    last_name='Doe',
    gender='INVALID_VALUE',
    birthdata='1991-01-01',
    interests=['travel', 'sports'],
    )

except ValidationError as e:
    print(str(e))


# invalid datetime
try: Person(
    first_name='John',
    last_name='Doe',
    gender='MALE',
    birthdata='1991-13-42',
    interests=['travel', 'sports'],
    )

except ValidationError as e:
    print(str(e))


class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str

class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]
    address: Address

try:
    Person(
        first_name="John",
        last_name="Doe",
        gender="INVALID_VALUE",
        birthdate="1991-01-01",
        interests=["travel", "sports"],
        address={
            "street_address": "12 Squirell Street",
            "postal_code": "424242",
            "city": "Woodtown",
            # Missing country
        }
    )
except ValidationError as e:
    print(str(e))