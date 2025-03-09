from fastapi import APIRouter, Depends, status
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..models import Users
from ..database import SessionLocal
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import jwt

router = APIRouter()


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name:str
    password:str
    role:str
    

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


def authenticate_user(username:str, password:str, db):
    user = db.query(Users).filter(Users.user_name == username).first()
    passwords = db.query(Users).filter(Users.hashed_password == password).first()
    if not user:
        return False
    if not passwords:
        return False
    # if not bcrypt_context.verify(password, user.hashed_password):
    #     return False
    return True


@router.post("/auth/", status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,create_user_request: CreateUserRequest):
    create_user_model = Users(
        email = create_user_request.email,
        user_name = create_user_request.username,
        first_name = create_user_request.first_name,
        last_name = create_user_request.last_name,
        role = create_user_request.role,
        hashed_password = create_user_request.password,
        is_active = True
    )
    
    db.add(create_user_model)
    db.commit() 
    
    
@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm,Depends()], db:db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return 'Failed Authentication'
    return 'Success Aunthentication'  
