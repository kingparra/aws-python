import click.testing
import pytest

from area_calc import console


@pytest.fixture
def runner():
    """Run command and return an object"""
    return click.testing.CliRunner()


def test_main_succeeds(runner):
    """Will area-calc without cli args exit with 2?"""
    assert runner.invoke(console.main).exit_code == 2


def test_help_returns_zero(runner):
    """Will running area-calc --help return exit code 0?"""
    assert runner.invoke(console.main, "--help").exit_code == 0
