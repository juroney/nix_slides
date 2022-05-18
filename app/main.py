from pathlib import Path

import uvicorn
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

prefix = "slides/"


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    resp = {
        'request': request,
        "title": "Linux Overview",
        "sub_title": "A very high-level overview",
        "next": "/agenda",
        "previous": "/"
    }
    return templates.TemplateResponse(f'{prefix}index.html', resp)


@app.get("/agenda", response_class=HTMLResponse)
async def agenda(request: Request):
    agenda_items = {
        "one": "Primary differences",
        "two": "Types of shells",
        "three": "Configuration profiles",
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
    return templates.TemplateResponse(f'{prefix}agenda.html', resp)


@app.get("/prim-diff", response_class=HTMLResponse)
async def prim_diff(request: Request):
    bullets = {
        "one": {
            "linux": "Born in 1991 - Linus Torvalds",
            "unix": "Dev begins in 1969 at Bell Laboratories - Dennis Ritchie, Ken Thompson "
        },
        "two": {
            "linux": "Refers to the Linux Kernel",
            "unix": "Refers to a proprietary OS"
        },
        "three": {
            "linux": "RedHat, Ubuntu, Fedora, FreeBSD",
            "unix": "Sun Solaris, AT&T System V, HP-UX, BSD"
        },
        "four": {
            "linux": "Free",
            "unix": "Available at a cost"
        },

    }

    resp = {
        "request": request,
        "title": "Primary Differences",
        "previous": "/agenda",
        "next": "/shells",
        "bullets": bullets
    }
    return templates.TemplateResponse(f'{prefix}prim-diff.html', resp)


@app.get("/shells", response_class=HTMLResponse)
async def shells(request: Request):
    shells = {
        "Login": "Initial login shell denoted with a hyphen (e.g. -zsh, -bash)",
        "Interactive": "Inherits from login shell. Sources user profile(s)",
        "Non-interactive": "Does not source user profiles. (e.g. call a script from a script)",
    }
    resp = {
        "request": request,
        "title": "Types of Shells",
        "previous": "/prim-diff",
        "next": "/config-files",
        "shells": shells,
    }

    return templates.TemplateResponse(f'{prefix}shells.html', resp)


@app.get("/config-files", response_class=HTMLResponse)
async def config_files(request: Request):
    config_files: dict = {
        '/etc/profile': 'System-wide profile for ksh, bash, etc.',
        '/etc/zprofile': 'System-wide profile for zsh',
        '$HOME/.zprofile': 'User profile. Sourced before .zshrc',
        '$HOME/.zshrc': 'User configuration for interactive shells',
    }
    resp = {
        "request": request,
        "title": "Configuration Profiles",
        "next": "/variables",
        "previous": "/shells",
        "config_files": config_files
    }
    return templates.TemplateResponse(f'{prefix}config-files.html', resp)

@app.get("/variables", response_class=HTMLResponse)
async def variables(request: Request):
    bullets: dict = {
        'Local': {
            'desc': 'Exists in the scope in which is was instantiated.',
            'ex': 'local BOXOFROCKS=10 declared inside a function is scoped only to that block of code'
        },
        'Environment': {
            'desc': 'Available to descendents',
            'ex': 'export VAR=important_value becomes available to descendents of the current shell'
        },
        'Shell': {
            'desc': 'Set and used by the shell',
            'ex': 'Shell variables can be either local or environment'
        }
    }
    resp = {
        "request": request,
        "title": "Variables",
        "next": "/path-environ",
        "previous": "/config-files",
        "bullets": bullets
    }
    return templates.TemplateResponse(f'{prefix}variables.html', resp)

@app.get("/path-environ", response_class=HTMLResponse)
async def environ(request: Request):
    bullets: list = [
        "Directly affects the shells ability to find commands",
        "Available to descendents",
        "Common and easy to modify",
        "Extremely important to the system as a whole"
    ]
    resp = {
        "request": request,
        "title": "PATH Environment Variable",
        "next": "/thanks",
        "previous": "/variables",
        "bullets": bullets
    }
    return templates.TemplateResponse(f'{prefix}environ.html', resp)

@app.get("/thanks", response_class=HTMLResponse)
async def thanks(request: Request):
    resp = {
        "request": request,
        "title": "Q & A",
        "next": "/",
        "previous": "/variables"
    }
    return templates.TemplateResponse(f'{prefix}thanks.html', resp)


if __name__ == '__main__':
    uvicorn.run(app)
