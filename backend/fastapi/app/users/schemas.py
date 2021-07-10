from typing import Any, Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from .models import User

PublicUser = pydantic_model_creator(
    User, name='PublicUser', exclude=(), include=()
)

PrivateUser = pydantic_model_creator(
    User, name="PrivateUser"
)
EditUser = pydantic_model_creator(
    User, name="EditUser", include=("fio", "avatar")
)


class Token(BaseModel):
    access_token: str
    token_type: str


class UserData(BaseModel):
    username: str
    password: str


class PublicHash(BaseModel):
    hash: str


class Success(BaseModel):
    ok: bool
    payload: Optional[Any] = None
