from datetime import datetime, timedelta
from typing import Optional, Union

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext

from .models import User
from .schemas import EditUser, PrivateUser, PublicUser, Token
from ..settings import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


async def authenticate_user(username: str, password: str) -> Union[User, None]:
    user = await User.get_or_none(email=username)
    if user is None:
        return None
    if not pwd_context.verify(password, user.hashed_password):
        return None
    return user


async def decode_token(token) -> str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username


async def get_user(token: str = Depends(oauth2_scheme)) -> User:
    email = decode_token(token)
    user = await User.get_or_none(email=email)
    if user is None:
        raise HTTPException(404, 'User not found')
    return user


def create_access_token(data, expires_data: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_data is not None:
        expire = datetime.utcnow() + expires_data
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_data=expires)
    return Token(access_token=access_token, token_type="bearer")


@router.post("/create", response_model=Token)
async def new_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_or_none(email=form_data.username)
    if user is not None:
        raise HTTPException(400, "User already exists")

    user = await User.create(
        email=form_data.username, hashed_password=pwd_context.hash(form_data.password)
    )

    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(data={"sub": user.email}, expires_data=expires)
    return Token(access_token=token, token_type='Bearer')


@router.get("/profile", response_model=PrivateUser)
async def profile(user: User = Depends(get_user)):
    return await PrivateUser.from_tortoise_orm(user)


@router.put("/", response_model=PrivateUser)
async def edit(edited: EditUser, user=Depends(get_user)):
    user = await user.update_from_dict(edited.dict())
    await user.save()
    return await PrivateUser.from_tortoise_orm(user)


@router.delete("/")
async def destroy(user=Depends(get_user)):
    await user.delete()
    return {"ok": True}


@router.get("/all")
async def all_users():
    return await PrivateUser.from_queryset(User.all())


@router.get("/{user_id}", response_model=PublicUser)
async def user_by_id(user_id: int):
    user = await User.get_or_none(id=user_id)
    if user:
        return await PublicUser.from_tortoise_orm(user)
    raise HTTPException(404, "User not found")
