from pydantic import ConfigDict
from sqlmodel import SQLModel

class DepartamentoCreate(SQLModel):
    name: str

class DepartamentoResponse(DepartamentoCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)

class DepartamentoUpdate(SQLModel):
    name: str | None = None

