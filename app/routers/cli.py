from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.utils import get_referer, config

router = APIRouter(prefix="/cli")


@router.get("/title", response_class=HTMLResponse)
async def cli(request: Request):
    resp: dict = {
        "request": request,
        "title": "Command Line Interface",
        "description": "Overview of commonly used cli tools",
        "sub_title": "Overview of commonly used cli tools",
        "next": f"{router.prefix}/agenda",
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.title_template, resp)


@router.get("/agenda", response_class=HTMLResponse)
async def agenda(request: Request):
    agenda_items = [
        "man",
        "ls",
        "cp",
        "mv",
        "touch",
        "rm",
    ]

    resp: dict = {
        'request': request,
        "title": "Agenda",
        "description": '"Agenda"',
        "previous": await get_referer(request),
        "next": f"{router.prefix}/man",
        "items": agenda_items,
    }

    return config.templates.TemplateResponse(config.bullet_template, resp)


@router.get("/man", response_class=HTMLResponse)
async def man(request: Request):
    bullets = [
        "Unsure how to use a command?",
        "Details of functionality",
        "Related commands",
        "Additional information",
    ]

    resp: dict = {
        "request": request,
        "title": "man",
        "description": '"The man command"',
        "code": "man cp",
        "command": "man",
        "next": f"{router.prefix}/man-example",
        "items": bullets,
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.bullet_template, resp)


@router.get("/man-example", response_class=HTMLResponse)
async def man_example(request: Request):
    resp: dict = {
        "request": request,
        "title": "man Example",
        "description": '"The man command"',
        "code": "man cp",
        "command": "man",
        "next": f"{router.prefix}/ls",
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.code_template, resp)


@router.get("/ls", response_class=HTMLResponse)
async def ls_command(request: Request):
    bullets = [
        "List files in a directory",
        "List files with varying details",
    ]

    resp: dict = {
        "request": request,
        "title": "ls",
        "description": '"The ls command"',
        "code": "ls -lathr",
        "next": f"{router.prefix}/ls-example",
        "items": bullets,
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.bullet_template, resp)


@router.get("/ls-example", response_class=HTMLResponse)
async def ls_example(request: Request):
    resp: dict = {
        "request": request,
        "title": "ls Example",
        "description": '"The ls command"',
        "code": "ls -lathr",
        "command": "man",
        "next": f"{router.prefix}/mkdir",
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.code_template, resp)


@router.get("/mkdir", response_class=HTMLResponse)
async def mkdir_command(request: Request):
    bullets = [
        "Create a new directory",
        "Create a new directory of directories",
    ]

    resp: dict = {
        "request": request,
        "title": "mkdir",
        "description": '"The mkdir command"',
        "code": "mkdir blips_and_chitz",
        "next": f"{router.prefix}/mkdir-example",
        "items": bullets,
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.bullet_template, resp)


@router.get("/mkdir-example", response_class=HTMLResponse)
async def mkdir_example(request: Request):
    resp: dict = {
        "request": request,
        "title": "mkdir Example",
        "description": '"The mkdir command"',
        "code": "mkdir -p parent/child_dir/",
        "command": "mkdir",
        "next": f"{router.prefix}/copy",
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.code_template, resp)


@router.get("/copy", response_class=HTMLResponse)
async def cp_command(request: Request):
    bullets = [
        "Copy files/directories from one location to another",
        "Optionally preserve permissions",
        "Rename file(s) at destination",
        "Recursively copy files",
    ]

    resp: dict = {
        "request": request,
        "title": "cp",
        "description": '"The cp command"',
        "items": bullets,
        "next": f"{router.prefix}/copy-example",
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.bullet_template, resp)


@router.get("/copy-example", response_class=HTMLResponse)
async def cp_example(request: Request):
    resp: dict = {
        "request": request,
        "title": "cp",
        "description": '"The cp command"',
        "code": "cp -p file1 file1_new_location",
        "next": f"{router.prefix}/move",
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.code_template, resp)


@router.get("/move", response_class=HTMLResponse)
async def move_command(request: Request):
    bullets = [
        "Not the same as cp",
        "Permanently move files from one location to another",
        "Move files or directories"
        "Rename at destination"
    ]

    resp: dict = {
        "request": request,
        "title": "mv",
        "description": '"The mv command"',
        "next": f"{router.prefix}/move-example",
        "items": bullets,
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.bullet_template, resp)


@router.get("/move-example", response_class=HTMLResponse)
async def move_example(request: Request):
    resp: dict = {
        "request": request,
        "title": "mv",
        "description": '"The mv command"',
        "code": "mv $HOME/file1 $HOME/file1_new_location",
        "next": f"{router.prefix}/touch",
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.code_template, resp)


@router.get("/touch", response_class=HTMLResponse)
async def touch_command(request: Request):
    bullets = [
        "Modify file modification and access times",
        "Create empty file with given name",
    ]

    resp: dict = {
        "request": request,
        "title": "touch",
        "description": '"The touch command"',
        "next": f"{router.prefix}/touch-example",
        "items": bullets,
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.bullet_template, resp)


@router.get("/touch-example", response_class=HTMLResponse)
async def touch_example(request: Request):
    resp: dict = {
        "request": request,
        "title": "touch",
        "description": '"The touch command"',
        "code": "touch placeholder.out",
        "next": f"{router.prefix}/title",
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.code_template, resp)
