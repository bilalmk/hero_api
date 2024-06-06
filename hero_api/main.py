from fastapi import Depends, FastAPI

from hero_api.routers import hero, team


app = FastAPI()
app.include_router(hero.router)
app.include_router(team.router)

@app.get("/")
async def root():
    return {"message": "Hello Dashboard Applications!"}

