import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from dotenv import load_dotenv
from models.user_model import User, UserInfo, UserCreate
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from typing import Optional
from datetime import datetime, timedelta
import os,pymongo

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt

def save_user(user):
    client = pymongo.MongoClient(
        host="localhost",
        port=27017,
    )
    db = client["your_database_name"]
    user_collection = db["users"]

    user_dict = user.dict()
    user_dict["password_hash"] = hash_password(user_dict.pop("password"))

    user_collection.insert_one(user_dict)

def get_user_by_email(email):
    client = pymongo.MongoClient(
        host="localhost",
        port=27017,
    )
    db = client["your_database_name"]
    user_collection = db["users"]

    user_dict = user_collection.find_one({"email": email})
    if user_dict:
        return User(**user_dict)
    return None

def authenticate_user(user: User):
    user = get_user_by_email(user.email)
    if not user or not verify_password(user.password, user.password_hash):
        return False
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return access_token

def create_user(user: UserCreate):
    hashed_password = hash_password(user.password)
    new_user = User(email=user.email, password_hash=hashed_password)
    save_user(new_user)
    return new_user

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user = get_user_by_email(email)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
