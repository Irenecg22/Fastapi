from fastapi import FastAPI

from app.db.session import engine
from app.routers import departamentos, empleados
from sqlmodel import SQLModel

app = FastAPI()

app.include_router(departamentos.router)
app.include_router(empleados.router)

def init_db():
    SQLModel.metadata.create_all(engine)

init_db()