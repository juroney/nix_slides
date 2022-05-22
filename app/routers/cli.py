from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse

from app.utils import get_app_config, get_referer

router = APIRouter(dependencies=[Depends(get_referer)])
config = get_app_config()


@router.get("/cli", response_class=HTMLResponse)
async def cli(request: Request):
    resp: dict = {
        "request": request,
        "title": "Code Block",
        "descriptions": '"Code Example"',
        "code": "echo y | docker container prune",
        "next": "/title",
        "previous": await get_referer(request),
    }

    return config.templates.TemplateResponse(f'{config.cli_prefix}/title.html', resp)
