from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    full_name: str
    age: int
    email: str
    password: str
    profile_image: Optional[str] = None
    updated_at: Optional[str] = None
    created_at: Optional[str] = None

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    email: str
    profile_image: Optional[str] = None
    is_paid: bool
    is_active: bool
    is_verified: bool
    subscription_type: Optional[str] = None
    subscription_start: Optional[str] = None
    subscription_end: Optional[str] = None
    balance: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True