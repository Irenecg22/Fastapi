from sqlmodel import create_engine, Session
from app.core.config import config

if config.database_url:
    database_url = config.database_url
else:
    database_url = "sqlite:///./database.db"

connect_args = {}
if database_url.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(database_url, echo=config.debug, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session