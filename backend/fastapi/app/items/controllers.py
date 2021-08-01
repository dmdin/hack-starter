from typing import List

from fastapi import APIRouter, Depends, HTTPException

from .models import Item
from .schemas import CreateItem, DeleteSuccess, ItemsSchema
from ..users.auth import get_user
from ..users.models import User

router = APIRouter()


async def check_item(id: str, user: User = Depends(get_user)):
    item = await Item.get_or_none(id=id)
    if item is None:
        raise HTTPException(404, 'Item not found')
    if item.user_id != user.id:
        raise HTTPException(403, 'User does not have access to this')
    return item


@router.get('/all', response_model=List[ItemsSchema])
async def get_all():
    return await ItemsSchema.from_queryset(Item.all())


@router.post('/', response_model=ItemsSchema)
async def create_item(new_item: CreateItem, user: User = Depends(get_user)):
    item = await Item.create(**new_item.dict(), user_id=user.id)
    return await ItemsSchema.from_tortoise_orm(item)


@router.get('/{id}', response_model=ItemsSchema)
async def get_my(item: Item = Depends(check_item)):
    return await ItemsSchema.from_tortoise_orm(item)


@router.put('/', response_model=ItemsSchema)
async def edit_item(edited_item: CreateItem, item: Item = Depends(check_item)):
    await item.update_from_dict(edited_item.dict())
    await item.save()
    return await ItemsSchema.from_tortoise_orm(item)


@router.delete('/')
async def delete_item(item: Item = Depends(check_item)):
    await item.delete()
    return DeleteSuccess(ok=True)
