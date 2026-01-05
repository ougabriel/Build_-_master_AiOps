#pydantic keeps the integrity of the data which has been defined in creation.

from pydantic import BaseModel

class User(BaseModel):
    id = int
    name = str
    is_active = bool

input_data = {'id': 12, 'name': "Gabriel", 'is_active': True}
user = User(**input_data)

print(user)