from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    nombre: str = Field(..., min_length=1, max_length=255)
    nivel_skate: int = Field(..., ge=1, le=5, description="Nivel de skate entre 1 y 5")


class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=100)
    
    @validator('nivel_skate')
    def validate_nivel_skate(cls, v):
        if v < 1 or v > 5:
            raise ValueError('El nivel de skate debe estar entre 1 y 5')
        return v


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    email: Optional[str] = None
