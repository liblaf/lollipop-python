import typer_di

from liblaf import lollipop

from . import hello

app = typer_di.TyperDI(name="lollipop")
lollipop.utils.add_command(app, hello.app)
