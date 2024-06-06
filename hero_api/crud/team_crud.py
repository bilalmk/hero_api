from fastapi import HTTPException
from sqlmodel import Session, select
from config import engine
from hero_api.models.team_hero_model import PublicTeamWithHero
from hero_api.models.team_model import CreateTeam, Team, UpdateTeam


def get_team_list():
    with Session(engine) as session:
        teams = session.exec(select(Team)).all()
        return teams


def get_team(team_id: int):
    with Session(engine) as session:
        team = session.get(Team, team_id)
        if not team:
            raise HTTPException(status_code=404, detail="Team not found")
        
        return PublicTeamWithHero.model_validate(team)
        #return team


def create_team(team: CreateTeam):
    with Session(engine) as session:
        db_team = Team.model_validate(team)
        session.add(db_team)
        session.commit()
        session.refresh(db_team)
        return db_team


def update_team(team: UpdateTeam, team_id: int):
    with Session(engine) as session:
        db_team = session.get(Team, team_id)
        if not db_team:
            raise HTTPException(status_code=404, detail="Team not found")

        team_data = team.model_dump(exclude_unset=True)
        db_team.sqlmodel_update(team_data)
        session.add(db_team)
        session.commit()
        session.refresh(db_team)
        return db_team


def delete_team(team_id: int):
    with Session(engine) as session:
        db_team = session.get(Team, team_id)
        if not db_team:
            raise HTTPException(status_code=404, detail="Team not found")

        session.delete(db_team)
        session.commit()
        return {"ok": True}
