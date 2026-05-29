from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import UserSignup
from ..schemas import UserLogin
from ..crud import create_user
from ..crud import get_user_by_email
from ..auth import hash_password
from ..auth import verify_password
router = APIRouter()
@router.post("/signup")
def signup(
    user: UserSignup,db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db,user.email)
    if existing_user:
        raise HTTPException(status_code=400,detail="Email already exists")
    hashed_password = hash_password(user.password)
    create_user(db, user.username,user.email, hashed_password)
    return {"message": "Signup successful"}

@router.post("/login")
def login(user: UserLogin,db: Session = Depends(get_db)):
    db_user = get_user_by_email( db,user.email)
    if not db_user:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    valid_password = verify_password(user.password,db_user.password)
    if not valid_password:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    return {"message": "Login successful"}
