from pathlib import Path

from fastapi.templating import Jinja2Templates
from pydantic import BaseConfig, BaseModel


class AppConfig(BaseModel):
    class Config(BaseConfig):
        arbitrary_types_allowed = True

    static_path: Path
    templates_dir: Path
    templates: Jinja2Templates
    title_slide: str
    slides_prefix: str
    overview_prefix: str
    cli_prefix: str
    bullet_slide: str
    two_column_table: str
    three_column_table: str
