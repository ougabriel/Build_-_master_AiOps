from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username: str
    password: str
    confirm_password: str

    @field_validator("username")
    def username_length(cls, value):
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters long.")
        return value

    @model_validator(mode="after")
    def passwords_match(cls, obj):
        if obj.password != obj.confirm_password:
            raise ValueError("Passwords do not match.")
        return obj

user_1 = User(username="jsmith", password="secure123", confirm_password="secure123")