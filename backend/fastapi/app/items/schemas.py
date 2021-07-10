from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Item

ItemsSchema = pydantic_model_creator(
    Item, name='ItemsSchema', exclude=(), include=()
)


class CreateItem(BaseModel):
    name: str
    desc: str
    pic: str


class DeleteSuccess(BaseModel):
    ok: bool
