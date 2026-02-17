from sqlmodel import Session, select
from fastapi import Depends, HTTPException

from app.db.session import get_session
from app.models.departamento import Departamento
from app.schemas.departamento import (DepartamentoCreate,DepartamentoResponse,DepartamentoUpdate)

class DepartamentoService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, data: DepartamentoCreate) -> DepartamentoResponse:
        dept = Departamento(**data.model_dump())
        self.session.add(dept)
        self.session.commit()
        self.session.refresh(dept)
        return DepartamentoResponse(**dept.model_dump())

    def get_all(self):
        return self.session.exec(select(Departamento)).all()

    def get_by_id(self, id: int):
        dept = self.session.get(Departamento, id)
        if not dept:
            raise HTTPException(404, "Departamento no encontrado")
        return dept

    def update(self, id: int, data: DepartamentoUpdate):
        dept = self.get_by_id(id)
        dept_data = data.model_dump(exclude_unset=True)

        for k, v in dept_data.items():
            setattr(dept, k, v)

        self.session.add(dept)
        self.session.commit()
        self.session.refresh(dept)
        return dept

    def delete(self, id: int):
        dept = self.get_by_id(id)
        self.session.delete(dept)
        self.session.commit()
        return {"message": "Departamento eliminado"}
