import os
from dotenv import load_dotenv
from sqlmodel import Session, create_engine

load_dotenv()

connection = os.environ.get("CONNECTION")
engine = create_engine(connection)  # type: ignore

def get_session():
    with Session(engine) as session:
        yield session
