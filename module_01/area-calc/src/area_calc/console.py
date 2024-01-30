import click

from area_calc import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """area-calc Command-line area calculator"""
    click.echo("Successful run!")
