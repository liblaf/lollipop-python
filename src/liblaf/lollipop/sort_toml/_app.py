from pathlib import Path
from typing import Annotated

import typer

from liblaf import lollipop

app: typer.Typer = lollipop.new_app("sort-toml")


@app.command()
def command(
    files: Annotated[list[Path], typer.Argument(exists=True, dir_okay=False)],
) -> None:
    from . import main

    main(files)
