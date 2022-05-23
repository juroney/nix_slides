from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse

from app.utils import get_referer, config

router = APIRouter(dependencies=[Depends(get_referer)])


@router.get("/cli", response_class=HTMLResponse)
async def cli(request: Request):
    resp: dict = {
        "request": request,
        "title": "Command Line Interface",
        "description": "Overview of commonly used cli tools",
        "sub_title": "Overview of commonly used cli tools",
        "next": "/man",
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(config.title_template, resp)


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
        "next": "#",
        "items": bullets,
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(f'{config.bullet_template}', resp)
