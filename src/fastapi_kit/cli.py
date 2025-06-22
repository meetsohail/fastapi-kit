import typer
from fastapi_kit.commands import startproject, startapp, generate_crud

app = typer.Typer()

# Flattened CLI commands
app.command()(startproject.startproject)
app.command()(startapp.startapp)
app.command()(generate_crud.generate_crud)

def main():
    app()

if __name__ == "__main__":
    main()
