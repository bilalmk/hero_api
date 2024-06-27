from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from config import sessionDep
from hero_api.models.hero_model import CreateHero, Hero, UpdateHero
from sqlalchemy.orm import joinedload

from hero_api.models.team_hero_model import PublicHeroWithTeam

class hero_crud:
    def __init__(self, session):
        self.session = session

    def get_hero_list(self):
        heros = self.session.exec(select(Hero)).all()
        return heros

    def get_hero(self, hero_id: int):
        # hero = session.exec(select(Hero).options(joinedload(Hero.team)).where(Hero.id == hero_id)).one()
        # return hero
        hero = self.session.get(Hero, hero_id)
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")

        return PublicHeroWithTeam.model_validate(hero)

    def create_hero(self, hero: CreateHero):
        db_hero = Hero.model_validate(hero)
        self.session.add(db_hero)
        self.session.commit()
        self.session.refresh(db_hero)
        return db_hero

    def update_hero(self, hero: UpdateHero, hero_id: int):
        db_hero = self.session.get(Hero, hero_id)
        if not db_hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        
        hero_data = hero.model_dump(exclude_unset=True)
        
        db_hero.sqlmodel_update(hero_data)
        self.session.add(db_hero)
        self.session.commit()
        self.session.refresh(db_hero)
        return db_hero

    def delete_hero(self, hero_id: int):
        hero = self.session.get(Hero, hero_id)
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")

        self.session.delete(hero)
        self.session.commit()
        return {"ok": True}