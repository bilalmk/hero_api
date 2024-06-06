from typing import Optional
from hero_api.models.hero_model import PublicHero
from hero_api.models.team_model import PublicTeam


class PublicTeamWithHero(PublicTeam):
    heroes: list["PublicHero"] = []
    
class PublicHeroWithTeam(PublicHero):
    team: Optional["PublicTeam"] = None