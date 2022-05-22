from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse

from app.utils import get_referer, get_app_config

router = APIRouter(dependencies=[Depends(get_referer)])

config = get_app_config()


@router.get("/title", response_class=HTMLResponse)
async def root(request: Request):
    resp: dict = {
        'request': request,
        "title": "Linux Overview",
        "description": '"A very high-level overview"',
        "sub_title": "A very high-level overview",
        "next": "/agenda",
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(f'{config.overview_prefix}/title.html', resp)


@router.get("/agenda", response_class=HTMLResponse)
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
        "description": '"Agenda"',
        "previous": await get_referer(request),
        "next": "/prim-diff",
        "items": agenda_items,
    }

    return config.templates.TemplateResponse(f'{config.overview_prefix}/{config.bullet_slide}', resp)


@router.get("/prim-diff", response_class=HTMLResponse)
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
        "description": "Primary differences between linux and unix",
        "previous": await get_referer(request),
        "next": "/shells",
        "thead_one": "Linux",
        "thead_two": "UNIX",
        "items": items,
    }

    return config.templates.TemplateResponse(f'{config.overview_prefix}/{config.two_column_table}', resp)


@router.get("/shells", response_class=HTMLResponse)
async def shells(request: Request):
    items: tuple = (
        ("Login", "Initial login shell denoted with a hyphen (e.g. -zsh, -bash)"),
        ("Interactive", "Inherits from login shell. Sources user profile(s)"),
        ("Non-interactive", "Does not source user profiles. (e.g. call a script from a script)"),
    )

    resp: dict = {
        "request": request,
        "title": "Types of Shells",
        "description": '"System Profile Slide"',
        "previous": await get_referer(request),
        "next": "/config-files",
        "thead_one": "Shell",
        "thead_two": "Description",
        "items": items,
    }

    return config.templates.TemplateResponse(f'{config.overview_prefix}/{config.two_column_table}', resp)


@router.get("/config-files", response_class=HTMLResponse)
async def config_files(request: Request):
    items: tuple = (
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
        "previous": await get_referer(request),
        "thead_one": "Profile",
        "thead_two": "Description",
        "items": items,
    }

    return config.templates.TemplateResponse(f'{config.overview_prefix}/{config.two_column_table}', resp)


@router.get("/variables", response_class=HTMLResponse)
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
        "previous": await get_referer(request),
        "thead_one": "Type",
        "thead_two": "Description",
        "thead_three": "Example",
        "items": bullets,
    }

    return config.templates.TemplateResponse(f'{config.overview_prefix}/{config.three_column_table}', resp)


@router.get("/path-environ", response_class=HTMLResponse)
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
        "description": '"PATH Environment Variable"',
        "next": "/epoch",
        "previous": await get_referer(request),
        "items": bullets,
    }

    return config.templates.TemplateResponse(f'{config.overview_prefix}/{config.bullet_slide}', resp)


@router.get("/epoch", response_class=HTMLResponse)
async def epoch(request: Request):
    bullets: list = [
        "The number of seconds since 1970-01-01 00:00:00 UTC",
        "Referred to as UNIX time, POSIX time, EPOCH time",
        "32-bit signed integer"
    ]

    resp: dict = {
        "request": request,
        "title": "What is the EPOCH?",
        "description": '"EPOCH"',
        "next": "/qanda",
        "previous": await get_referer(request),
        "items": bullets,
    }

    return config.templates.TemplateResponse(f'{config.overview_prefix}/{config.bullet_slide}', resp)


@router.get("/qanda", response_class=HTMLResponse)
async def qanda(request: Request):
    resp: dict = {
        "request": request,
        "title": "Q & A",
        "title_override_super_large_text": True,
        "descriptions": '"Questions and Answers"',
        "next": "/cli",
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(f'{config.overview_prefix}/qanda.html', resp)
