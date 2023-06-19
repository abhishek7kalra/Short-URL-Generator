from datetime import datetime
from pydantic import BaseModel

class Url(BaseModel):
    hash: str
    original_url: str
    creation_date: datetime
    expiration_date: datetime
    user_id: int
