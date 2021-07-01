import json
import os
from glob import glob

current_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(current_path, '.gitignore'), 'r', encoding='utf8') as file:
    exclude = set(file for file in file.read().split('\n'))

folders = list(
    set([folder.replace('\\', '/').replace("app/", "").strip('/') for folder in glob('app/*/')]) - exclude
)

apps = {
    folder: {
        'models': [f'app.{folder.replace("/", ".")}.models']
    }
    for folder in folders
}

PROD_TORTOISE_ORM = {
    'connections': {'default': f'sqlite://{current_path}/db/prod/db.sqlite3'},
    'apps': apps,
    # 'apps': {'models': model_paths},
}

TEST_TORTOISE_ORM = {
    'connections': {'default': f'sqlite://{current_path}/db/test/db.sqlite3'},
    'apps': apps,
    # 'apps': {'models': model_paths},
}

with open(os.path.join(current_path, 'secrets.json')) as file:
    secrets = json.load(file)

SECRET_KEY = secrets.get('SECRET_KEY')  # TODO Define SECRET_KEY in json
EMAIL_PASSWORD = secrets.get('EmailPassword')  # TODO Define SECRET_KEY in json
EMAIL_ADDRESS = 'hack.masters@mail.ru'

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = 'HS256'
CORS_ORIGINS = ['*']
IS_PROD = os.getenv('IS_PROD', False)
DOMAIN = os.getenv('DOMAIN', 'set.prod.domain.com')
