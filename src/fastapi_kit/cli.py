import typer
from fastapi_kit.commands import startproject, startapp, generate_crud

app = typer.Typer()
app.add_typer(startproject.app, name="startproject")
app.add_typer(startapp.app, name="startapp")
app.add_typer(generate_crud.app, name="generate-crud")

def main():
    app()

if __name__ == "__main__":
    main()
