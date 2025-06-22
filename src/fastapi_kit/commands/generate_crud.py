import os
import typer

def generate_crud(model_name: str, app: str = "apps"):
    """
    Generate model, schema, crud, and route for a given resource.
    """
    model_file = f"{app}/{model_name.lower()}/models.py"
    schema_file = f"{app}/{model_name.lower()}/schemas.py"
    crud_file = f"{app}/{model_name.lower()}/crud.py"
    routes_file = f"{app}/{model_name.lower()}/routes.py"

    os.makedirs(os.path.dirname(model_file), exist_ok=True)

    with open(model_file, "w") as f:
        f.write(f"""\
from sqlalchemy import Column, Integer, String
from core.db import Base

class {model_name}(Base):
    __tablename__ = "{model_name.lower()}s"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
""")

    with open(schema_file, "w") as f:
        f.write(f"""\
from pydantic import BaseModel

class {model_name}Base(BaseModel):
    name: str

class {model_name}Create({model_name}Base):
    pass

class {model_name}Out({model_name}Base):
    id: int

    class Config:
        orm_mode = True
""")

    with open(crud_file, "w") as f:
        f.write(f"""\
from sqlalchemy.orm import Session
from .models import {model_name}
from .schemas import {model_name}Create

def create_{model_name.lower()}(db: Session, obj_in: {model_name}Create):
    db_obj = {model_name}(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
""")

    with open(routes_file, "a") as f:
        f.write(f"""\
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import crud, schemas
from core.db import get_db

router = APIRouter()

@router.post("/{model_name.lower()}/")
def create_{model_name.lower()}(item: schemas.{model_name}Create, db: Session = Depends(get_db)):
    return crud.create_{model_name.lower()}(db=db, obj_in=item)
""")

    typer.echo(f"✅ CRUD for '{model_name}' generated under '{app}/{model_name.lower()}/'")
