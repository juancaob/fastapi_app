from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

# Shape the user's request (the user sending data to us)

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

# Shape our response to the user (us sending data to the user)

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

# Shape the user's request (the user sending data to us)

class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Shape our response to the user (us sending data to the user)



class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

