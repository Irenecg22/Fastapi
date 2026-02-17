from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Empleado(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str | None= None
    puesto: str | None= None
    imageUri: str | None= None

    departamentoId: int | None = Field(default=None, foreign_key="departamento.id")
    departamento: Optional["Departamento"] = Relationship(back_populates="empleados")
