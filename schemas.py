from typing import Optional

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    username: str
    email: Optional[EmailStr] = None

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    password: str


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
