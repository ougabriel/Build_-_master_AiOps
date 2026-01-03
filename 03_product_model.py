from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True  # default value

# valid
product_one = Product(id=12, name="Gabriel", price=24.55, in_stock=True)

# valid (uses default in_stock=True)
product_two = Product(id=12, name="Gabriel", price=24.55)

# ❌ invalid (missing required fields)
product_three = Product(name="Gabriel")
