import typer


def add_command(app: typer.Typer, command: typer.Typer) -> None:
    if (
        len(command.registered_commands) == 1
        and command.registered_commands[0].name is None
        and command.registered_commands[0].callback is not None
    ):
        app.command(name=command.info.name)(command.registered_commands[0].callback)
    else:
        app.add_typer(command)
