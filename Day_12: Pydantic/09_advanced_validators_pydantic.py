from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    # User class inheriting from BaseModel to create a data model for user with validation
    username: str          # Field for the username which must be a string
    password: str          # Field for the password which must be a string
    confirm_password: str  # Field for confirming the password

    @field_validator("username")
    def username_length(cls, value):
        # Validator to check that the username length is at least 3 characters
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters long")  # Raise error if condition fails
        return value  # Return the validated value

    @model_validator(mode="after")
    def passwords_match(cls, values):
        # Validator to ensure that the password and confirm_password match
        if values['password'] != values['confirm_password']:
            raise ValueError("Passwords do not match")  # Raise error if passwords do not match
        return values  # Return validated values

# Example usage to create an instance of User
user = User(username="jsmith", password="secure123", confirm_password="secure123")