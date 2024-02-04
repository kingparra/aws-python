import click
import sys

from csv_merge.merge import process_files


# TODO Add option for custom column renames by overriding mappings
@click.command()
@click.option("--input", "-i", type=click.File(), multiple=True,
              help="path(s) to CSV files to merge")
@click.option("--output", "-o", type=click.Path(),
              help="file name to save merged CSV as")
def main(input, output):
    if input is None or output is None:
        click.echo("Missing value for the --input or --output option.")
        sys.exit(2)
    else:
        process_files(input, output)
