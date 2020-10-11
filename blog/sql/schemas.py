from typing import Any, Optional

import peewee
from pydantic import BaseModel, constr
from pydantic.utils import GetterDict

string255 = constr(max_length=255)
string32 = constr(max_length=32)


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class UserBase(BaseModel):
    username: string32
    password: str


class UserCreate(UserBase):
    ...


class UserUpdate(BaseModel):
    id: int
    password: Optional[string255] = None
    email: Optional[string255] = None


class User(BaseModel):
    id: int
    username: string32
    email: Optional[string255] = None
    nickname: Optional[string255] = None
    token: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class TagBase(BaseModel):
    title: string32


class TagCreate(TagBase):
    author_id: int


class TagUpdate(TagBase):
    id: int
    author_id: int


class TagDelete(BaseModel):
    id: int


class Tag(TagBase):
    id: int
    author: User

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class CatalogBase(BaseModel):
    title: str


class CatalogCreate(CatalogBase):
    author_id: int


class Catalog(CatalogBase):
    id: int
    author: User

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class CatalogUpdate(CatalogCreate):
    id: int


class CatalogDelete(BaseModel):
    id: int


class CommentBase(BaseModel):
    content: str


class CommentUpdate(CommentBase):
    id: int


class CommentCreate(CommentBase):
    author_id: int


class Comment(CommentBase):
    id: int
    author: User

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class CommentDelete(BaseModel):
    id: int


class PostBase(BaseModel):
    title: string32
    content: str
    slug: string32
    summary: string255


class PostCreate(PostBase):
    author_id: int
    status: Optional[int] = 0
    can_comment: Optional[bool] = True


class PostUpdate(PostCreate):
    id: int


class PostDelete(BaseModel):
    id: int


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
