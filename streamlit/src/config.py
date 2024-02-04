"""Config"""

import os
from pathlib import Path

from pydantic_settings import BaseSettings

FILE = Path(__file__)
ROOT = str(FILE.parent.parent)
APP_DIR = FILE.parent.absolute()
PROJECT_DIR = APP_DIR.parent.absolute()


class Settings(BaseSettings):
    """Settings"""

    API_URL: str

    class Config:
        """Settings config"""

        extra = 'ignore'
        env_file = os.path.join(ROOT, '.env')


class AppSettings(BaseSettings):
    """App settings"""

    PAGE_EMOJI: str = ':grinning:'

    class Config:
        """App settings config"""

        extra = 'ignore'
        env_file = os.path.join(ROOT, '.env')


settings = Settings()
app_settings = AppSettings()
