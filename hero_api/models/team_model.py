from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from hero_api.models.hero_model import Hero

class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str


class Team(TeamBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    heroes: list["Hero"] = Relationship(back_populates="team")

class CreateTeam(TeamBase):
    pass

class PublicTeam(TeamBase):
    id: int
    
class UpdateTeam(SQLModel):
    id: int | None = None
    name: str | None = Field(default=None)
    headquarters: str | None = Field(default=None)
    
