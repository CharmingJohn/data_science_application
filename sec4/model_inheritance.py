from pydantic import BaseModel

class PostCreate(BaseModel):
    id: int
    title: str
    content: str

class PostPublic(BaseModel):
    id: int
    title: str
    content: str

class PostDB(BaseModel):
    id: int
    title: str
    content: str
    nb_views: int=0

class PostBase(BaseModel):
    title: str
    content: str

    def excerpt(self) -> str:
        return '{}...'.format(self.content[:140])

class PostCreate(PostBase):
    pass

class PostPublic(PostBase):
    id: int

class PostDB(PostBase):
    id: int
    nb_views: int=0