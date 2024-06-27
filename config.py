import os
from typing import Annotated
from dotenv import load_dotenv
from fastapi import Depends
from sqlmodel import Session, create_engine

load_dotenv()

connection = os.environ.get("CONNECTION")
engine = create_engine(connection)  # type: ignore


def get_session():
    with Session(engine) as session:
        yield session

sessionDep = Annotated[Session, Depends(get_session)]
