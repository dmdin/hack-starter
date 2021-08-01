import os
import pathlib

import click
import inflect
from jinja2 import Template

p = inflect.engine()


@click.group()
def app():
    pass


@app.command('create')
@click.argument('app_name', required=False)
def create_app(app_name: str):
    if app_name is None:
        app_name: str = click.prompt(click.style('Set the name of new app', bold=True, fg='blue'), default='default')

    singular = p.singular_noun(app_name)
    if not singular:
        singular = app_name
    single, Single = singular.lower(), singular.capitalize()

    plural = p.plural_noun(app_name)
    if not plural:
        plural = app_name
    many, Many = plural.lower(), plural.capitalize()

    template_path = pathlib.Path('./template')
    target_path = pathlib.Path(f'./app/{many}')
    target_path.mkdir(parents=True, exist_ok=True)

    for file_name in os.listdir(template_path):
        with open(template_path / file_name, 'r', encoding='utf8') as file:
            content = Template(file.read()).render(single=single, Single=Single, many=many, Many=Many)
        with open(target_path / file_name.rstrip('.template'), 'w', encoding='utf8') as file:
            file.write(content)

    click.secho(f'Created app "{many}"', fg='magenta', bold=True)


if __name__ == '__main__':
    # python tools.py create
    app()
