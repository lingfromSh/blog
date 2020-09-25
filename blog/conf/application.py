import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

########################
#   INIT APPLICATION
########################

from conf import set_project_config

set_project_config(os.environ["blog-setting"])


@app.on_event("startup")
async def startup():
    ...


@app.on_event("shutdown")
async def shutdown():
    ...


########################
# API ROUTING REGISTRY
########################
from api import router as api_router
from pages import router as page_router

app.include_router(api_router, prefix="/api/v1")
app.include_router(page_router)

