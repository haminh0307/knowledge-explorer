"""Prompt"""

def extract_keywords_prompt(text: str):
    """Return OpenAI API messages to extract keywords"""
    return [
        {
            "role": "system",
            "content": "You will be provided with a block of text, and your task is to extract a list of keywords from it.",
        },
        {
            "role": "user",
            "content": text,
        }
    ]

def definition_prompt(keyword: str):
    """Return OpenAI API messages to get definition of keyword"""
    return [
        {
            "role": "system",
            "content": "You will be provided with a keyword, and your task is to give its definition in a short paragraph.",
        },
        {
            "role": "user",
            "content": keyword,
        }
    ]

def quiz_prompt(keyword: str):
    """Return OpenAI API messages to get a random quiz of keyword"""
    return [
        {
            "role": "system",
            "content": "You will be provided with a keyword, and your task is to give a single-choice quiz with 4 answer. See the following json format: {\"question\":\"\",\"options\":[],\"answer\":\"\"}",
        },
        {
            "role": "user",
            "content": keyword,
        }
    ]