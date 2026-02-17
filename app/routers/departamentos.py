from fastapi import APIRouter, Depends

from app.schemas.departamento import (DepartamentoCreate,DepartamentoResponse,DepartamentoUpdate)
from app.services.departamentoServices import DepartamentoService

router = APIRouter(prefix="/departamentos", tags=["Departamentos"])




@router.post("/", response_model=DepartamentoResponse)
async def create(data: DepartamentoCreate, service: DepartamentoService = Depends()):
 return service.create(data)


@router.get("/", response_model=list[DepartamentoResponse])
async def read_all(service: DepartamentoService = Depends()):
    return service.get_all()


@router.get("/{id}", response_model=DepartamentoResponse)
async def read_one(id: int, service: DepartamentoService = Depends()):
    return service.get_by_id(id)

@router.patch("/{id}", response_model=DepartamentoResponse)
async def update(id: int, data: DepartamentoUpdate, service: DepartamentoService = Depends()):
    return service.update(id, data)

@router.delete("/{id}")
async def delete(id: int, service: DepartamentoService = Depends()):
    return service.delete(id)
