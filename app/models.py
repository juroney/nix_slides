from pathlib import Path

from fastapi.templating import Jinja2Templates
from pydantic import BaseConfig, BaseModel


class AppConfig(BaseModel):
    class Config(BaseConfig):
        arbitrary_types_allowed = True

    static_path: Path
    templates_dir: Path
    templates: Jinja2Templates
    title_template: str
    code_template: str
    bullet_template: str
    two_column_template: str
    three_column_template: str
