# DirectorioAPI – Backend con FastAPI + SQLModel

API REST desarrollada con **FastAPI** y **SQLModel** que gestiona un directorio de empleados y departamentos.

Esta API está diseñada para conectar con una aplicación cliente desarrollada en .NET MAUI y permite realizar operaciones completas de CRUD sobre las entidades **Empleado** y **Departamento**.
La aplicación está preparada para funcionar tanto con **SQLite** como con **PostgreSQL**, dependiendo de si se configura o no la variable de entorno correspondiente.

## Características

-  CRUD completo de Empleados
-  CRUD completo de Departamentos
-  Arquitectura en capas (routers, services, models, schemas)
-  Soporte para SQLite
-  Soporte para PostgreSQL mediante variable de entorno
-  Contenerización con Docker
-  Documentación automática con Swagger

---

## Tecnologías utilizadas

- FastAPI
- SQLModel
- SQLite
- PostgreSQL
- Uvicorn
- Docker
- Pydantic

---

## Estructura del Proyecto

Api/
│
├── app/
│ ├── core/
│ ├── db/
│ ├── models/
│ │ ├── empleado.py
│ │ └── departamento.py
│ │
│ ├── routers/
│ │ ├── empleados.py
│ │ └── departamentos.py
│ │
│ ├── schemas/
│ │ ├── empleado.py
│ │ └── departamento.py
│ │
│ ├── services/
│ │ ├── empleadoServices.py
│ │ └── departamentoServices.py
│ │
│ └── main.py
│
├── database.db
├── Dockerfile
├── docker-compose.yml
└── requirements.txt


---

## Configuración de Base de Datos

La aplicación detecta automáticamente qué base de datos usar:

-  Si **NO** existe la variable `DATABASE_URL` → usa **SQLite**
-  Si existe `DATABASE_URL` → usa **PostgreSQL**

---



## Disponibilidad
La API estará disponible en:

http://127.0.0.1:8000

## Ejecutar la aplicación 

http://127.0.0.1:8000/docs
 Docker
 Construir la imagen
Desde la raíz del proyecto:
docker build -t directorio_api .

Ejecutar con SQLite (por defecto)
docker run -d -p 8000:8000 directorio_api
Ejecutar con PostgreSQL
docker run -d -p 8000:8000 \
-e DATABASE_URL="postgresql://postgres:123456@host.docker.internal:5432/directorio" \
directorio_api

Docker Compose (opcional con PostgreSQL)
Si utilizas docker-compose.yml:

docker-compose up --build

## Endpoints principales

Empleados
GET /empleados
GET /empleados/{id}
POST /empleados
PUT /empleados/{id}
DELETE /empleados/{id}

Departamentos
GET /departamentos
GET /departamentos/{id}
POST /departamentos
PUT /departamentos/{id}
DELETE /departamentos/{id}

## Arquitectura
La aplicación está organizada en capas:

Models → Definición de tablas SQLModel
Schemas → Validación de datos
Services → Lógica de negocio
Routers → Endpoints
DB → Configuración de base de datos
Main → Inicialización de la aplicación

Esto permite mantener el código limpio, modular y escalable.

## Conexión con .NET MAUI
Esta API está diseñada para ser consumida por la aplicación cliente desarrollada en .NET MAUI, que consulta el directorio de empleados y departamentos mediante peticiones HTTP.

## Autor
Irene Cañada Gómez.
Desarrollo de Aplicaciones Multiplataforma
Práctica FastAPI + SQLModel + Docker

