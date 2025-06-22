import os
import typer

app = typer.Typer()

@app.command()
def create(app_name: str, path: str = "apps"):
    """
    Create a new app module inside the project.
    """
    app_path = os.path.join(path, app_name)

    if os.path.exists(app_path):
        typer.echo(f"App {app_name} already exists.")
        raise typer.Exit()

    os.makedirs(app_path)
    files = ["__init__.py", "models.py", "schemas.py", "routes.py", "crud.py"]

    for file in files:
        with open(os.path.join(app_path, file), "w") as f:
            if file == "routes.py":
                f.write(f"""\
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_{app_name}():
    return {{"message": "This is the {app_name} module"}}
""")
            else:
                f.write("")

    typer.echo(f"✅ App '{app_name}' created at {app_path}.")
