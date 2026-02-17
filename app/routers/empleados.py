from fastapi import APIRouter, Depends
from app.services.empleadoServices import EmpleadoService
from app.schemas.empleado import (EmpleadoCreate,EmpleadoResponse,EmpleadoUpdate)

router = APIRouter(prefix="/empleados", tags=["Empleados"])

@router.post("/", response_model=EmpleadoResponse)
async def create(data: EmpleadoCreate, service: EmpleadoService = Depends()):
    return service.create(data)

@router.get("/", response_model=list[EmpleadoResponse])
async def read_all(departamentoId: int | None = None, service: EmpleadoService = Depends()):
    return service.get_all(departamentoId)

@router.get("/{id}", response_model=EmpleadoResponse)
async def read_one(id: int, service: EmpleadoService = Depends()):
    return service.get_by_id(id)

@router.patch("/{id}", response_model=EmpleadoResponse)
async def update(id: int, data: EmpleadoUpdate, service: EmpleadoService = Depends()):
    return service.update(id, data)

@router.delete("/{id}")
async def delete(id: int, service: EmpleadoService = Depends()):
    return service.delete(id)
