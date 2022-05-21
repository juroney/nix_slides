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

prefix = "slides"


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    resp: dict = {
        'request': request,
        "title": "Linux Overview",
        "sub_title": "A very high-level overview",
        "next": "/agenda",
        "previous": "/"
    }
    return templates.TemplateResponse(f'{prefix}/index.html', resp)


@app.get("/agenda", response_class=HTMLResponse)
async def agenda(request: Request):
    agenda_items = [
        "Primary differences",
        "Types of shells",
        "Configuration profiles",
        "Important variables",
        "EPOCH",
    ]
    resp: dict = {
        'request': request,
        "title": "Agenda",
        "previous": "/",
        "next": "/prim-diff",
        "items": agenda_items,
    }
    return templates.TemplateResponse(f'{prefix}/agenda.html', resp)


@app.get("/prim-diff", response_class=HTMLResponse)
async def prim_diff(request: Request):
    items: tuple = (
        (
            "Born in 1991 - Linus Torvalds",
            "Dev begins in 1969 at Bell Laboratories - Dennis Ritchie, Ken Thompson"
        ),
        (
            "Refers to the Linux Kernel",
            "Refers to a proprietary OS"
        ),
        (
            "RedHat, Ubuntu, Fedora, FreeBSD",
            "Sun Solaris, AT&T System V, HP-UX, BSD"
        ),
        (
            "Free",
            "Available at a cost"
        ),
    )

    resp: dict = {
        "request": request,
        "title": "Primary Differences",
        "previous": "/agenda",
        "next": "/shells",
        "thead_one": "Linux",
        "thead_two": "UNIX",
        "items": items,
    }
    return templates.TemplateResponse(f'{prefix}/prim-diff.html', resp)


@app.get("/shells", response_class=HTMLResponse)
async def shells(request: Request):
    shells: dict = {
        "Login": "Initial login shell denoted with a hyphen (e.g. -zsh, -bash)",
        "Interactive": "Inherits from login shell. Sources user profile(s)",
        "Non-interactive": "Does not source user profiles. (e.g. call a script from a script)",
    }
    resp: dict = {
        "request": request,
        "title": "Types of Shells",
        "description": '"System Profile Slide"',
        "previous": "/prim-diff",
        "next": "/config-files",
        "thead_one": "Shell",
        "thead_two": "Description",
        "shells": shells,
    }

    return templates.TemplateResponse(f'{prefix}/shells.html', resp)


@app.get("/config-files", response_class=HTMLResponse)
async def config_files(request: Request):
    config_files: tuple = (
        (
            '/etc/profile',
            'System-wide profile for ksh, bash, etc.'
        ),
        (
            '/etc/zprofile',
            'System-wide profile for zsh'
        ),
        (
            '$HOME/.zprofile',
            'User profile. Sourced before .zshrc'
        ),
        (
            '$HOME/.zshrc',
            'User configuration for interactive shells'
        ),
    )
    resp: dict = {
        "request": request,
        "title": "Configuration Profiles",
        "description": '"System Profile Slide"',
        "next": "/variables",
        "previous": "/shells",
        "thead_one": "Profile",
        "thead_two": "Description",
        "items": config_files
    }
    return templates.TemplateResponse(f'{prefix}/config-files.html', resp)


@app.get("/variables", response_class=HTMLResponse)
async def variables(request: Request):
    bullets: dict = {
        'Local': {
            'col_two': 'Exists in the scope in which is was instantiated',
            'col_three': 'local BOXOFROCKS=10 declared inside a function is scoped only to that block of code'
        },
        'Environment': {
            'col_two': 'Available to descendents',
            'col_three': 'export VAR=important_value becomes available to descendents of the current shell'
        },
        'Shell': {
            'col_two': 'Set and used by the shell',
            'col_three': 'Shell variables can be either local or environment'
        }
    }
    resp: dict = {
        "request": request,
        "title": "Variables",
        "description": '"Types of Variables"',
        "next": "/path-environ",
        "previous": "/config-files",
        "header_one": "Type",
        "header_two": "Description",
        "header_three": "Example",
        "items": bullets
    }
    return templates.TemplateResponse(f'{prefix}/variables.html', resp)


@app.get("/path-environ", response_class=HTMLResponse)
async def environ(request: Request):
    bullets: list = [
        "Directly affects the shells ability to find commands",
        "Available to descendents",
        "Common and easy to modify",
        "Extremely important to the system as a whole"
    ]
    resp: dict = {
        "request": request,
        "title": "PATH Environment Variable",
        "next": "/epoch",
        "previous": "/variables",
        "items": bullets,
    }
    return templates.TemplateResponse(f'{prefix}/environ.html', resp)


@app.get("/epoch", response_class=HTMLResponse)
async def epoch(request: Request):
    bullets: list = [
        "The number of seconds since 1970-01-01 00:00:00 UTC",
        "Referred to as UNIX time, POSIX time, EPOCH time",
        "32-bit signed integer"
    ]
    resp: dict = {
        "request": request,
        "title": "What is EPOCH?",
        "next": "/qanda",
        "previous": "/path-environ",
        "bullets": bullets
    }
    return templates.TemplateResponse(f'{prefix}/epoch.html', resp)


@app.get("/qanda", response_class=HTMLResponse)
async def thanks(request: Request):
    resp: dict = {
        "request": request,
        "title": "Q & A",
        "next": "/",
        "previous": "/variables"
    }
    return templates.TemplateResponse(f'{prefix}/qanda.html', resp)


if __name__ == '__main__':
    uvicorn.run(app)
