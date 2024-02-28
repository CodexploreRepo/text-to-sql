from fastapi import Depends, FastAPI
from logzero import logger
from typing_extensions import Annotated

from . import config
from .routers import llm

settings = config.get_settings()

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    contact=settings.app_owner,
)

app.include_router(llm.router, prefix="/llm")


@app.get("/")
async def root(
    settings: Annotated[config.Settings, Depends(config.get_settings)]
):

    return {"app_name": settings.app_name}
