"""FastAPI main"""

from config import settings
from service.router import router
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi import FastAPI, Request, status


app = FastAPI(title='Knowledge explorer API')


origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_headers=settings.CORS_HEADERS,
    allow_credentials=True,
    allow_methods=["*"],
)


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Validation exception handler"""

    details = exc.errors()
    error_details = []

    for error in details:
        error_details.append({'error': error['msg'] + " " + str(error['loc'])})

    return JSONResponse(content={'message': error_details})


@app.get('/', include_in_schema=False)
def root() -> None:
    """Redirect to docs"""
    return RedirectResponse('/docs')


@app.get('/health', status_code=status.HTTP_200_OK, tags=['health'])
def healthcheck() -> None:
    """Health check"""
    return JSONResponse(content={'message': 'success'})


app.include_router(router, tags=['service'])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host=settings.HOST, port=settings.PORT, reload=True)
