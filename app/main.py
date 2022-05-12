from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


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
    resp = {
        'request': request,
        "title": "Agenda",
        "previous": "/",
        "next": "/prim-diff",
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
    resp = {
        "request": request,
        "title": "Types of Shells",
        "previous": "/prim-diff",
        "next": "/config-files",
    }
    return templates.TemplateResponse('shells.html', resp)


@app.get("/config-files", response_class=HTMLResponse)
async def config_files(request: Request):
    resp = {
        "request": request,
        "title": "Config Files",
        "next": "/thanks",
        "previous": "/shells"
    }
    return templates.TemplateResponse('config-files.html', resp)


@app.get("/thanks", response_class=HTMLResponse)
async def thanks(request: Request):
    resp = {
        "request": request,
        "title": "Config Files",
        "next": "/",
        "previous": "/config-files"
    }
    return templates.TemplateResponse('thanks.html', resp)
