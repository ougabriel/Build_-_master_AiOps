from pydantic import BaseModel
from typing import List, Dict, Optional


class cart(BaseModel):
    id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None #accepts a string as constant but can pass if not available

