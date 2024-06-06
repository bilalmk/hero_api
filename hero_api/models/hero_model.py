from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from hero_api.models.team_model import Team

class BaseHero(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
    team_id: int | None = Field(default=None, foreign_key="team.id")

class Hero(BaseHero, table=True):
    id: int | None = Field(default=None, primary_key=True)
    team: Optional["Team"] = Relationship(back_populates="heroes")
    
class CreateHero(BaseHero):
    pass

class PublicHero(BaseHero):
    id: int
    
class UpdateHero(SQLModel):
    name: str | None = None
    secret_name: str | None = None
    age: int | None = None
    team_id: int | None = None