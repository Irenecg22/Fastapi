from linecache import cache

from sqlmodel import Session, select
from fastapi import Depends, HTTPException

from app.db.session import get_session
from app.models.empleado import Empleado
from app.schemas.empleado import (EmpleadoCreate,EmpleadoResponse,EmpleadoUpdate)

class EmpleadoService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, data: EmpleadoCreate) -> EmpleadoResponse:
        emp = Empleado(**data.model_dump())
        self.session.add(emp)
        self.session.commit()
        self.session.refresh(emp)
        return EmpleadoResponse(**emp.model_dump())

    def get_all(self, departamento_id: int | None = None):
        query = select(Empleado)

        if departamento_id is not None:
            query = query.where(Empleado.departamento_id == departamento_id)

        return self.session.exec(query).all()

    def get_by_id(self, id: int):
        emp = self.session.get(Empleado, id)
        if not emp:
            raise HTTPException(404, "Empleado no encontrado")
        return emp

    def update(self, id: int, data: EmpleadoUpdate):
        emp = self.get_by_id(id)
        emp_data = data.model_dump(exclude_unset=True)

        for k, v in emp_data.items():
            setattr(emp, k, v)

        self.session.add(emp)
        self.session.commit()
        self.session.refresh(emp)
        return emp

    def delete(self, id: int):
        emp = self.get_by_id(id)
        self.session.delete(emp)
        self.session.commit()
        return {"message": "Empleado eliminado"}
