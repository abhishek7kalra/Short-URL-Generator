from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from models.user_model import User, UserCreate, UserInfo
from auth import create_user, authenticate_user, get_current_user
import pymongo
router = APIRouter()

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/signup", response_model=UserInfo)
async def sign_up(user: UserCreate):
    # Create a new user
    new_user = create_user(user)
    return new_user

@router.post("/login")
async def sign_in(user: User):
    # Authenticate the user
    token = authenticate_user(user)
    if not token:
        return {"error": "Invalid credentials"}
    return {"access_token": token, "token_type": "bearer"}

@router.get("/profile", response_model=UserInfo)
async def get_profile(current_user: User = Depends(get_current_user)):
    # Return the user profile
    return current_user