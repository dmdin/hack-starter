import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rich.console import Console
from tortoise import Tortoise

from .items.controllers import router as items_router
from .settings import CORS_ORIGINS, DOMAIN, IS_PROD, PROD_TORTOISE_ORM, TEST_TORTOISE_ORM
from .users.controllers import router as users_router

# print(COLOR_SYSTEMS)
console = Console(color_system="windows")

if IS_PROD:
    config_var = PROD_TORTOISE_ORM
else:
    config_var = TEST_TORTOISE_ORM


def prepare_db():
    # Удаляем папку с тестовой базой данных при запуске и импорте
    current_path = os.path.dirname(os.path.realpath(__file__))
    test_db_path = os.path.join(current_path, "db", "test")
    prod_db_path = os.path.join(current_path, "db", "prod")
    # try:
    #     shutil.rmtree(test_db_path)
    # except FileNotFoundError:
    #     console.print('Directory "db" is not detected', style='bold red')

    for path in [test_db_path, prod_db_path]:
        Path(path).mkdir(parents=True, exist_ok=True)


async def startup():
    try:
        await Tortoise.init(config=config_var)
        await Tortoise.generate_schemas(safe=True)
    except Exception as ex:
        print(ex)


async def shutdown():
    await Tortoise.close_connections()


def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    prepare_db()

    app.include_router(users_router, prefix="/users", tags=["Users"])
    app.include_router(items_router, prefix="/items", tags=["Items"])
    app.add_event_handler("startup", startup)
    app.add_event_handler("shutdown", shutdown)

    if IS_PROD:
        console.print(f'Docs link: https://{DOMAIN}/docs', style='bold blue')
    else:
        console.print('Docs link: http://localhost:8000/docs', style='bold blue')

    return app
