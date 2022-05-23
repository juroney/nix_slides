import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.routers import cli, overview
from app.utils import config

app = FastAPI()

app.include_router(overview.router)
app.include_router(cli.router)

app.mount("/static", StaticFiles(directory=config.static_path), name="static")


@app.get("/")
async def index():
    return RedirectResponse('/title')


if __name__ == '__main__':
    uvicorn.run("main:app")
