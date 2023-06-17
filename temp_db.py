from typing import Dict
from pydantic import BaseModel

url_store: Dict[str, str] = {}

class URLRequest(BaseModel):
    url: str