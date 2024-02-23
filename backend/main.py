from fastapi import Depends, FastAPI
from typing_extensions import Annotated

from . import config

app = FastAPI()


@app.get("/")
async def root(
    settings: Annotated[config.Settings, Depends(config.get_settings)]
):
    return {"app_name": settings.app_name, "admin_email": settings.admin_email}
