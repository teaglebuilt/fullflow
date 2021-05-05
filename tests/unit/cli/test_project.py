import os
import sys
from fullflow.cli import cli


def test_project_created_with_template(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["init", "project_test", "--template", "kubernetes"])
        assert result.exit_code == 0
