import typer

import liblaf.lollipop as lollipop  # noqa: PLR0402

from . import hello, sort_toml

app: typer.Typer = lollipop.new_app("lollipop")
lollipop.add_command(app, hello.app)
lollipop.add_command(app, sort_toml.app)
