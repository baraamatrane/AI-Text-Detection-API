# app/crud.py
from sqlalchemy.orm import Session
from models.Usermodel import User 
from schema.UserSchema import UserCreate
from utils.hash import hash_password, verify_password
from utils.tokenjwt import create_access_token   

def create_user(db: Session, user: UserCreate):
    payload = user.model_dump()
    print("Payload before hashing:", payload["password"])
    payload["password"] = hash_password(payload["password"])
    payload["token"] = create_access_token(payload)
    db_user = User(**payload)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def sign_in(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if user and verify_password(password, user.password):
        return create_access_token(user.model_dump())
    return None

def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for key, value in user.model_dump().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user