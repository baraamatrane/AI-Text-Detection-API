from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from controlers import userCon
from schema.UserSchema import UserCreate, UserResponse
from database import get_db

UserRouter = APIRouter(prefix="/auth", tags=["auth"])


@UserRouter.post("/signup", response_model=UserResponse)
async def create_user_root(user: UserCreate, db: Session = Depends(get_db)):
    return userCon.create_user(db, user)

@UserRouter.post("/signin")
async def signin_user(email: str, password: str, db: Session = Depends(get_db)):
    user = userCon.sign_in(db, email, password)
    if user:
        return {"message": "User signed in successfully", "user": user}
    return {"message": "Invalid email or password"}, 401


@UserRouter.put("/{user_id}")
async def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return userCon.update_user(db, user_id, user)
