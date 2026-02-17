from pydantic import ConfigDict
from sqlmodel import SQLModel


class EmpleadoCreate(SQLModel):
    name: str
    puesto: str
    imageUri: str | None = None
    departamentoId: int | None = None


class EmpleadoResponse(SQLModel):
    id: int
    name: str
    puesto: str
    imageUri: str | None = None
    departamentoId: int | None = None

    model_config = ConfigDict(from_attributes=True)


class EmpleadoUpdate(SQLModel):
    name: str | None = None
    puesto: str | None = None
    imageUri: str | None = None
    departamentoId: int | None = None
