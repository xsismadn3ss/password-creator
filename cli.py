import click
from hashlib import sha256
import colorama
import random
import string

def encrypt(value: str):
    return sha256(value.encode()).hexdigest()

@click.group()
def cli():
    """DESCIPTION - create password and its hash\n
    DETAILS - The hash method used on this CLI is SHA256"""
    pass

@click.command()
@click.option(
    "--password", prompt="write your password", help="enter custom password"
)
def custom(password: str):
    """Create custom password"""
    hashed_password = encrypt(password)
    colorama.init()
    click.echo(
        "hash generated: "
        + colorama.Fore.GREEN
        + hashed_password
        + colorama.Style.RESET_ALL
    )
    click.echo()

@click.command()
def generate():
    """Create random password"""
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
        + encrypt(password)
        + colorama.Style.RESET_ALL
    )
    click.echo()

# Registrar los comandos en el grupo
cli.add_command(custom)
cli.add_command(generate)

# Punto de entrada principal
if __name__ == "__main__":
    cli()
