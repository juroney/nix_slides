from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

path = Path('app').absolute()
static_path = path / "static"
templates_dir = path / "templates"

app.mount("/static", StaticFiles(directory=static_path), name="static")
templates = Jinja2Templates(directory=templates_dir)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    resp = {
        'request': request,
        "title": "*nix Overview",
        "next": "/agenda",
        "previous": "/"
    }
    return templates.TemplateResponse('index.html', resp)


@app.get("/agenda", response_class=HTMLResponse)
async def agenda(request: Request):
    agenda_items = {
        "one": "Primary differences between Unix and Linux",
        "two": "Types of shells",
        "three": "Configuration files",
        "four": "Your shell environment",
        "five": "Configure your environment",
    }
    resp = {
        'request': request,
        "title": "Agenda",
        "previous": "/",
        "next": "/prim-diff",
        "agenda": agenda_items,
    }
    return templates.TemplateResponse('agenda.html', resp)


@app.get("/prim-diff", response_class=HTMLResponse)
async def prim_diff(request: Request):
    resp = {
        "request": request,
        "title": "Primary Differences",
        "previous": "/agenda",
        "next": "/shells",
    }
    return templates.TemplateResponse('prim-diff.html', resp)


@app.get("/shells", response_class=HTMLResponse)
async def shells(request: Request):
    shells = {
        "Login": "When you login, this is what you get. Sources /etc/{z}profile",
        "Interactive": "Inherits from login shell. Sources user configs",
        "Non-interactive": "Does not source user configs. (e.g. script calls a script)",
    }
    resp = {
        "request": request,
        "title": "Types of Shells",
        "previous": "/prim-diff",
        "next": "/config-files",
        "shells": shells,
    }

    return templates.TemplateResponse('shells.html', resp)


@app.get("/config-files", response_class=HTMLResponse)
async def config_files(request: Request):
    config_files: dict = {
        '/etc/profile': 'system configuration for ksh, bash, etc.',
        '/etc/zprofile': 'system configuration for zsh',
        '$HOME/.zprofile': 'user configuration. Sourced before .zshrc',
        '$HOME/.zshrc': 'user configuration for interactive shells',
    }
    resp = {
        "request": request,
        "title": "Config Files",
        "next": "/thanks",
        "previous": "/shells",
        "config_files": config_files
    }
    return templates.TemplateResponse('config-files.html', resp)


@app.get("/thanks", response_class=HTMLResponse)
async def thanks(request: Request):
    resp = {
        "request": request,
        "title": "Q & A",
        "next": "/",
        "previous": "/config-files"
    }
    return templates.TemplateResponse('thanks.html', resp)
