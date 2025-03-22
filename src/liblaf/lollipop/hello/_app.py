from typing import Annotated

import typer

from liblaf import lollipop

app: typer.Typer = lollipop.new_app("hello")


@app.command()
def command(name: Annotated[str, typer.Argument()] = "world") -> None:
    from . import main

    main(name)
