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
        referer: str = f"/{request.headers.get('referer').split('/')[-1]}"
    except AttributeError:
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
    slides_prefix = "slides"
    overview_prefix = f"{slides_prefix}/overview"
    cli_prefix = f"{slides_prefix}/cli_intro"

    config = AppConfig(
        static_path=static_path,
        templates_dir=templates_dir,
        templates=Jinja2Templates(directory=templates_dir),
        slides_prefix=slides_prefix,
        title_slide="title",
        overview_prefix=overview_prefix,
        cli_prefix=cli_prefix,
        bullet_slide="one_column_no_header_title_block.html",
        two_column_table="two_column_header_title_block.html",
        three_column_table="three_column_header_title_block.html"
    )

    return config
