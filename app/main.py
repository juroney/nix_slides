import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.models import AppConfig
from app.routers import cli, overview
from app.utils import get_app_config

app = FastAPI()

app.include_router(overview.router)
app.include_router(cli.router)

config: AppConfig = get_app_config()

app.mount("/static", StaticFiles(directory=config.static_path), name="static")


@app.get("/")
async def index():
    return RedirectResponse(config.title_slide)


if __name__ == '__main__':
    uvicorn.run("main:app")
