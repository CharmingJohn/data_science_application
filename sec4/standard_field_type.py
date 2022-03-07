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
    age: int

