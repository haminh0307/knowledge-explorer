"""Config"""

import os
from pathlib import Path
from pydantic_settings import BaseSettings


FILE = Path(__file__)
ROOT = str(FILE.parent.parent)


class Settings(BaseSettings):
    """Settings"""

    HOST: str
    PORT: int
    CORS_ORIGINS: list[str]
    CORS_HEADERS: list[str]

    class Config:
        """Settings config"""

        extra = 'ignore'
        env_file = os.path.join(ROOT, '.env')


settings = Settings()
