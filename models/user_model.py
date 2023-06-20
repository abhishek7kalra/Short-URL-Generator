from datetime import datetime
from pydantic import BaseModel

class UserInfo(BaseModel):
    id: str
    name: str
    email: str
    creation_date: str
    last_login: str

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class User(UserCreate):
    id: str