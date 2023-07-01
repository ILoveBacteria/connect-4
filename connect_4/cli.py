from connect_4 import __app_name__, __version__
from typing import Optional
from .ai import q_learning
import typer


app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    _: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return


@app.command()
def train(
    count_games: int = typer.Option(
        "--count-games",
        "-cg",
        prompt="Train the agent",
    ),
) -> None:
    q_learning.train(count_games)
