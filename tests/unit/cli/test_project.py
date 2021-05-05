import os
import sys
from fullflow.cli import cli



def test_project_created_with_template(runner, fake_root_dir):
    sys.path = [str(fake_root_dir), str(fake_root_dir / "src")] + sys.path
    result = runner.invoke(cli, ["init", "project_test", "--template", "kubernetes"])
    assert os.path.isdir(f"{fake_root_dir}/project_test")
    assert result.exit_code == 0
