from functools import lru_cache
from fastapi import FastAPI
from starlette.responses import Response

from api import crud
from config import Settings


app = FastAPI()
app.include_router(crud.router)


@lru_cache()
def get_settings():
    return Settings()


@app.get("/")
async def root():
    data = 'Hello world!'
    return Response(content=data, media_type="text/html")