from fastapi import APIRouter, HTTPException

from hero_api.crud.team_crud import create_team, delete_team, get_team, get_team_list, update_team
from hero_api.models.team_hero_model import PublicTeamWithHero
from hero_api.models.team_model import CreateTeam, PublicTeam, UpdateTeam

router = APIRouter(
    prefix="/api/team",
    tags=["team"],
    dependencies=[],
    responses={404: {"description": "Not Found"}},
)


@router.get("/", response_model=list[PublicTeam])
async def get():
    try:
        teams = get_team_list()
        return teams
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{team_id}", response_model=PublicTeamWithHero)
async def get_single_team(team_id: int):
    try:
        team = get_team(team_id)
        return team
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create", response_model=PublicTeam)
async def create(team: CreateTeam):
    try:
        dbTeam = create_team(team)
        return dbTeam
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{team_id}", response_model=PublicTeam)
async def update(team: UpdateTeam, team_id: int):
    try:
        db_team = update_team(team, team_id)
        return db_team
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.delete("/{team_id}")
async def delete(team_id: int):
    try:
        return delete_team(team_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
