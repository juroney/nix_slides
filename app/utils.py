import re
from pathlib import Path

from fastapi import Request
from fastapi.templating import Jinja2Templates

from app.models import AppConfig


async def get_referer(request: Request) -> str:
    """
    Get referer of a request.

    :param request:
    :return:
    """

    try:
        referer_header: str = request.headers.get('referer').split(':')
        referer = re.sub(r'[0-9]+', '', referer_header[-1])
    except (AttributeError, TypeError):
        referer = '/title'

    return referer


def get_app_config() -> AppConfig:
    """
    Create an object with config parameters
    required for the app.

    :return:
    """

    path = Path('app').absolute()
    static_path = path / "static"
    templates_dir = path / "templates"

    config = AppConfig(
        static_path=static_path,
        templates_dir=templates_dir,
        templates=Jinja2Templates(directory=templates_dir),
        title_template="title.html",
        code_template="code_example.html",
        bullet_template="one_column_no_header_title_block.html",
        two_column_template="two_column_header_title_block.html",
        three_column_template="three_column_header_title_block.html"
    )

    return config


config = get_app_config()
