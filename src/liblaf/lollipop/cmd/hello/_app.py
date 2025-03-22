from typing import Annotated

import typer
import typer_di

app = typer_di.TyperDI(name="hello")


@app.command()
def command(name: Annotated[str, typer.Argument()] = "world") -> None:
    print(f"Hello, {name}!")
