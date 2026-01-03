from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True #gives a constant value of True

    product_one = Product(id = 12, name = "Gabriel", price = 24.55, in_stock = True)

    product_two = Product(id = 12, name = "Gabriel", price = 24.55)

    #the code below will throw an error because it is expecting other values
    product_three = Product(name = "Gabriel")


