import os
import shutil
import typer

app = typer.Typer()

@app.command()
def create(project_name: str):
    """
    Create a new FastAPI project with core structure.
    """
    if os.path.exists(project_name):
        typer.echo(f"Project {project_name} already exists.")
        raise typer.Exit()

    os.makedirs(f"{project_name}/apps")
    os.makedirs(f"{project_name}/core")

    with open(f"{project_name}/main.py", "w") as f:
        f.write("""\
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastForge!"}
""")

    with open(f"{project_name}/core/__init__.py", "w") as f:
        f.write("")

    typer.echo(f"✅ Project '{project_name}' created.")
