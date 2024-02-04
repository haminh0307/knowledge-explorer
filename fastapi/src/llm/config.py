"""Config"""

import os
from pathlib import Path
from pydantic_settings import BaseSettings


FILE = Path(__file__)
ROOT = str(FILE.parent.parent.parent)

class LLMSettings(BaseSettings):
    """LLM settings"""

    OPENAI_API_KEY: str = 'OpenAI API key [read](https://platform.openai.com/account/api-keys)'

    class Config:
        """Settings config"""

        extra = 'ignore'
        env_file = os.path.join(ROOT, '.env')


llm_settings = LLMSettings()
