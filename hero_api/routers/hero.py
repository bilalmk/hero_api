from typing import Annotated, List
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Request
from sqlmodel import Session
from config import get_session, sessionDep
from hero_api.crud.hero_crud import hero_crud
# from hero_api.crud.hero_crud import (
#     create_hero,
#     delete_hero,
#     get_hero,
#     get_hero_list,
#     update_hero,
# )
from hero_api.models.hero_model import CreateHero, PublicHero, UpdateHero
from hero_api.models.team_hero_model import PublicHeroWithTeam

def get_hero_crud(session: sessionDep) -> hero_crud:
    return hero_crud(session)
    
router = APIRouter(
    prefix="/api/hero",
    tags=["hero"],
    responses={404: {"description": "Not found"}}   
)


@router.get("/", response_model=List[PublicHero])
async def get(hero_crud=Depends(get_hero_crud)):
    try:
        heros = hero_crud.get_hero_list()
        return heros
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{hero_id}", response_model=PublicHeroWithTeam)
async def get_single_hero(hero_id: int, hero_crud=Depends(get_hero_crud)):
    try:
        hero = hero_crud.get_hero(hero_id)
        return hero
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create", response_model=PublicHero)
async def create(hero: CreateHero, hero_crud=Depends(get_hero_crud)):
    try:
        public_hero = hero_crud.create_hero(hero)
        return public_hero
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/update/{hero_id}", response_model=PublicHero)
async def update(hero: UpdateHero, hero_id: int, hero_crud=Depends(get_hero_crud)):
    try:
        public_hero = hero_crud.update_hero(hero, hero_id)
        return public_hero
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete/{hero_id}")
async def delete(hero_id: int, hero_crud=Depends(get_hero_crud)):
    try:
        return hero_crud.delete_hero(hero_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
