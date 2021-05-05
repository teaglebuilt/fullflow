import sys
import shutil
import pkg_resources
from pathlib import Path
from termcolor import colored
import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('project_name')
@click.option('--template', required=False, help="Project template")
def init(project_name: str, template: str = 'kubernetes'):
    project_path = Path(
        pkg_resources.resource_filename('fullflow', 'starters')) / template
    dest = Path.cwd() / project_name
    shutil.copytree(str(project_path), str(dest))
    print(colored(f"Initializing Project {project_name} at {dest}", "blue"))
