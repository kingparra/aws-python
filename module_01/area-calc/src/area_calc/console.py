import click

from area_calc import __version__
from area_calc.calc import area, perim


@click.command()
@click.option("--height", type=str, help="height of the rectangle", required=True)
@click.option("--width", type=str, help="width of the rectangle", required=True)
@click.version_option(version=__version__)
def main(height, width):
    """area-calc : Calculate area of rectangle given height and width"""
    click.echo(f"height={height}, width={width}, " +
               f"area={area(height, width):P}, perimeter={perim(height, width):P}")
