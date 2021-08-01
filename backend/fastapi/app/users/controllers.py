from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from .auth import authenticate_user, create_token, get_user, pwd_context
from .models import User
from .schemas import EditUser, PrivateUser, PublicUser, Token, UserData
from ..settings import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()


@router.post('/token', response_model=Token)
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_token(data={'sub': user.email}, expires_data=expires)
    return Token(access_token=access_token, token_type='Bearer')


@router.post('/login', response_model=Token)
async def login(login_data: UserData):
    user = await authenticate_user(**login_data.dict())
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_token(data={'sub': user.email}, expires_data=expires)
    return Token(access_token=access_token, token_type='Bearer')


@router.post('/', response_model=Token)
async def new_user(reg_data: UserData):
    user = await User.get_or_none(email=reg_data.username)
    if user is not None:
        raise HTTPException(400, 'User already exists')

    user = await User.create(
        email=reg_data.username, hashed_password=pwd_context.hash(reg_data.password)
    )

    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_token(data={'sub': user.email}, expires_data=expires)
    return Token(access_token=token, token_type='Bearer')


@router.get('/profile', response_model=PrivateUser)
async def profile(user: User = Depends(get_user)):
    return await PrivateUser.from_tortoise_orm(user)


@router.put('/', response_model=PrivateUser)
async def edit(edited: EditUser, user=Depends(get_user)):
    user = await user.update_from_dict(edited.dict())
    await user.save()
    return await PrivateUser.from_tortoise_orm(user)


@router.delete('/')
async def destroy(user=Depends(get_user)):
    await user.delete()
    return {'ok': True}


@router.get('/all')
async def all_users():
    return await PrivateUser.from_queryset(User.all())


@router.get('/{user_id}', response_model=PublicUser)
async def user_by_id(user_id: int):
    user = await User.get_or_none(id=user_id)
    if user:
        return await PublicUser.from_tortoise_orm(user)
    raise HTTPException(404, 'User not found')
