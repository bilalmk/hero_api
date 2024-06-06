from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from config import engine
from hero_api.models.hero_model import CreateHero, Hero, UpdateHero
from sqlalchemy.orm import joinedload

from hero_api.models.team_hero_model import PublicHeroWithTeam


def get_hero_list():
    with Session(engine) as session:
        heros = session.exec(select(Hero)).all()
        return heros


def get_hero(hero_id: int):
    with Session(engine) as session:
        # hero = session.exec(select(Hero).options(joinedload(Hero.team)).where(Hero.id == hero_id)).one()
        # return hero
        hero = session.get(Hero, hero_id)
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")

        return PublicHeroWithTeam.model_validate(hero)

def create_hero(hero: CreateHero):
    with Session(engine) as session:
        db_hero = Hero.model_validate(hero)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero


def update_hero(hero: UpdateHero, hero_id: int):
    with Session(engine) as session:
        db_hero = session.get(Hero, hero_id)
        if not db_hero:
            raise HTTPException(status_code=404, detail="Hero not found")

        hero_data = hero.model_dump(exclude_unset=True)
        db_hero.sqlmodel_update(hero_data)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero

def delete_hero(hero_id: int):
    with Session(engine) as session:
        hero = session.get(Hero, hero_id)
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")

        session.delete(hero)
        session.commit()
        return {"ok": True}
