from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    creation_date: datetime
    last_login: datetime