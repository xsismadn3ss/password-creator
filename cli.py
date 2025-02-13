import click
import hashlib
import colorama
import random
import string
from dataclasses import dataclass
from typing import Any


@dataclass
class Sha:
    name: str
    encrypt: Any


options = [
    Sha("sha224", lambda value: hashlib.sha224(str(value).encode()).hexdigest()),
    Sha("sha256", lambda value: hashlib.sha256(str(value).encode()).hexdigest()),
]


@click.group()
def cli():
    """
    -------------------- COMPRES SV --------------------\n
    DESCIPTION - create password and its hash\n
    DETAILS - The hash method used on this CLI is SHA256"""
    pass


@click.command()
@click.option(
    "--password", prompt="write your password: ", help="enter custom password"
)
@click.option(
    "--sha",
    default=2,
    prompt="""Select a hash algorithm
options:
    1 - sha224
    2 - sha256
default """,
    help="""options:
    1:sha224
    2:sha256
    default:2 """,
)
def custom(password: str, sha: int):
    """Create custom password"""
    hash = options[sha-1]
    hashed_password = hash.encrypt(password)
    colorama.init()
    click.echo(
        "hash generated: "
        + colorama.Fore.GREEN
        + hashed_password
        + colorama.Style.RESET_ALL
    )
    click.echo(
        "hash algorithm: " + colorama.Fore.GREEN + hash.name + colorama.Style.RESET_ALL
    )
    click.echo()


@click.command()
@click.option(
    "--sha",
    default=2,
    prompt="""Select a hash algorithm
options:
    1 - sha224
    2 - sha256
default """,
    help="""options:
    1:sha224
    2:sha256
    default:2 """,
)
def generate(sha: int):
    """Create random password"""
    hash = options[sha-1]
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    colorama.init()
    click.echo(
        "Secure password created: "
        + colorama.Fore.GREEN
        + password
        + colorama.Style.RESET_ALL
    )
    click.echo(
        "Password hash: "
        + colorama.Fore.GREEN
        + hash.encrypt(password)
        + colorama.Style.RESET_ALL
    )
    click.echo(
        "hash algorithm: " + colorama.Fore.GREEN + hash.name + colorama.Style.RESET_ALL
    )
    click.echo()


# Registrar los comandos en el grupo
cli.add_command(custom)
cli.add_command(generate)

# Punto de entrada principal
if __name__ == "__main__":
    cli()
