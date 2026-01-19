from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

    role: str = "user" 

class UserResponse(UserBase):
    id: int
    is_active: bool
    role: str 
    class Config:
        from_attributes = True