from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    is_paid = Column(Boolean, default=0)
    is_active = Column(Boolean, default=1)
    is_verified = Column(Boolean, default=0)
    subscription_type = Column(String, nullable=True)
    subscription_start = Column(String, nullable=True)
    subscription_end = Column(String, nullable=True)
    profile_image = Column(String, nullable=True)
    balance= Column(Integer, default=0)
    