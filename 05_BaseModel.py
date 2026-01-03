from pydantic import BaseModel
from typing import List, Dict, Optional


class Cart(BaseModel):
    id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None #accepts a string as constant but can pass if not available


cart_data = {
    "user_id": 123,
    "items": ["Laptop", "Mouse", "Keyboard", "Joystick"],
    "quantities": {"Laptop": 2, "Mouse": 13, "Keyboard": 12, "Joystick": 2}

}

cart = Cart(**cart_data)