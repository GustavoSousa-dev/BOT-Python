from pydantic import BaseModel
from typing import Optional, List


class Message(BaseModel):
    type: str
    from_phone: str
    body: Optional[str] = None
    media_url: Optional[str] = None
    question: Optional[str] = None
    options: Optional[List[str]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None