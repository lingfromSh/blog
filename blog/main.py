from fastapi import FastAPI

app = FastAPI()

########################
#    INIT DATABASE
########################

db_settings = {"DATABASE_URL": "sqlite:///blog.db"}


########################
#   INIT PROJECT
########################


@app.on_event("startup")
async def startup():
    ...


@app.on_event("shutdown")
async def shutdown():
    ...


########################
# API ROUTING REGISTRY
########################
from api import router

app.include_router(router, prefix="/api/v1")

########################
#  STARTING CONTROL
########################

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=8088, reload=True)
