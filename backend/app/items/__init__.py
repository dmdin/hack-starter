from tortoise import Tortoise

from .controllers import router


def init(app):
    app.include_router(router, prefix="/items", tags=["Items"])
    Tortoise.init_models(["app.items.models"], "items")
