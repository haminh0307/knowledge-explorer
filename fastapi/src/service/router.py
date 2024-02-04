"""Router for LLM services"""

import json
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from llm.llm import get_llm_service
from .prompt import extract_keywords_prompt, definition_prompt, quiz_prompt


router = APIRouter()


@router.post('/keywords')
def extract_keywords(
    content: str,
) -> JSONResponse:
    """
    The function calls the LLM service and returns the extracted keywords.
    """

    llm_service = get_llm_service()
    messages = extract_keywords_prompt(content)

    try:
        response = llm_service.call_service(messages)
    except Exception:
        return JSONResponse(content={'message': 'LLM service call error'})

    return JSONResponse(
        content={
            'message': 'success',
            'result': response.split(', '),
        }
    )


@router.post('/definitions')
def find_definition(
    keyword: str,
) -> JSONResponse:
    """
    The function calls the LLM service and returns the definition of the keyword.
    """

    llm_service = get_llm_service()
    messages = definition_prompt(keyword)

    try:
        response = llm_service.call_service(messages)
    except Exception:
        return JSONResponse(content={'message': 'LLM service call error'})

    return JSONResponse(
        content={
            'message': 'success',
            'result': response,
        }
    )


@router.post('/quizzes')
def random_quiz(
    keyword: str,
) -> JSONResponse:
    """
    The function calls the LLM service and returns a random quiz related to the keyword.
    """

    llm_service = get_llm_service()
    messages = quiz_prompt(keyword)

    try:
        response = llm_service.call_service(messages)
    except Exception:
        return JSONResponse(content={'message': 'LLM service call error'})

    response = json.loads(response)

    return JSONResponse(
        content={
            'message': 'success',
            'result': response,
        }
    )
