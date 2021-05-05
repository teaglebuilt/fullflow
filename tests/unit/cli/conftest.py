import tempfile
from pathlib import Path
from click.testing import CliRunner
from pytest import fixture


@fixture(scope="module")
def runner():
    yield CliRunner()

@fixture(scope="session")
def fake_root_dir():
    try:
        with tempfile.TemporaryDirectory() as tmp_root:
            yield Path(tmp_root)
    except PermissionError:  # pragma: no cover
        pass

@fixture(scope="session")
def fake_project_path(fake_root_dir):
    project_path = fake_root_dir / "project_test"
    return project_path