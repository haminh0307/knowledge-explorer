"""This file contains llm services"""

from abc import ABC, abstractmethod

import openai

from .config import llm_settings

class LLMService(ABC):
    """Abstract class for LLMService"""

    @classmethod
    @abstractmethod
    def call_service(cls, messages) -> str:
        """Abstract class method calling LLM service"""
        raise NotImplementedError


class OpenAIGPT(LLMService):
    """LLMService class of OpenAIGPT"""

    client = openai.OpenAI(api_key=llm_settings.OPENAI_API_KEY)

    @classmethod
    def call_service(cls, messages):
        response = cls.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5,
            max_tokens=64,
            top_p=1
        ).choices[0].message.content

        return response


def get_llm_service(model: str = 'OpenAIGPT') -> LLMService:
    """This function returns an instance of LLM service based on the model parameter"""

    llm_services = {
        'OpenAIGPT': OpenAIGPT,
    }

    return llm_services[model]
