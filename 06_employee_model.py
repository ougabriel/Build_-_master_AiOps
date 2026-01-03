
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_Length=3,
        max_length=50
        description="Employee Name"
        examples="Gabriel Okom"
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge = 10000  # ge means GreaterEqualsTo
            )

class User(BaseModel):
    email: str = Field (..., regex=r'')
    phone: str = Field (..., regex=r'')
    age: int = Field(
        ...,
        ge = 0,
        le = 150,
        description = "Age in years",
    )
    discount: int = Field(
        le = 0,
        ge = 100,
        description="Discount percentage"
    )