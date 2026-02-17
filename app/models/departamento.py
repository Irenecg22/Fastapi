from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

class Departamento(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str | None= None
    empleados: List["Empleado"] = Relationship(back_populates="departamento")

