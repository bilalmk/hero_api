from typing import List
from fastapi import APIRouter, HTTPException
from hero_api.crud.hero_crud import create_hero, delete_hero, get_hero, get_hero_list, update_hero
from hero_api.models.hero_model import CreateHero, PublicHero, UpdateHero
from hero_api.models.team_hero_model import PublicHeroWithTeam

router = APIRouter(
    prefix="/api/hero",
    tags=["hero"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[PublicHero])
async def get():
    try:
        heros = get_hero_list()
        return heros
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{hero_id}", response_model=PublicHeroWithTeam)
async def get_single_hero(hero_id: int):
    try:
        hero = get_hero(hero_id)
        return hero
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/create", response_model=PublicHero)
async def create(hero: CreateHero):
    try:
        public_hero = create_hero(hero)
        return public_hero
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/update/{hero_id}", response_model=PublicHero)
async def update(hero: UpdateHero, hero_id: int):
    try:
        public_hero = update_hero(hero, hero_id)
        return public_hero
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/delete/{hero_id}")
async def delete(hero_id: int):
    try:
        return delete_hero(hero_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

