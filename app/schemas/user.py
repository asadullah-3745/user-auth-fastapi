from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    # @field_validator("password")
    # @classmethod
    # def validate_password(cls, v):
    #     if len(v) < 8:
    #         raise ValueError("Password must be at least 8 characters")
    #     return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
