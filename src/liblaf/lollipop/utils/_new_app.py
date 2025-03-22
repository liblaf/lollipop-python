import typer
import typer_di


def new_app(name: str | None = None) -> typer.Typer:
    app = typer_di.TyperDI(name=name)
    return app
