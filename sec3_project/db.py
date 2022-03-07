from typing import Dict

from sec3_project.models.user import User
from sec3_project.models.post import Post


class DummyDatabase:
    users: Dict[int, User] = {}
    posts: Dict[int, Post] = {}


db = DummyDatabase()