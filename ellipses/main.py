import click

import ellipses.config as config
import ellipses.error as error
from ellipses.logging import logger


@error.print_on_error
@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def main(count, name):
    config.init()
