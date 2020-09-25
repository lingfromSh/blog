from typing import Optional
from fastapi import APIRouter, Depends, Header
from fastapi.security import OAuth2PasswordBearer
from sql import schemas, crud, database, models
from sql.database import db_state_default
from core import exceptions

database.db.connect()
database.db.create_tables([models.User, models.Post, models.Catalog, models.Tag, models.PostCatalog, models.PostTag])
database.db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()
sleep_time = 10


async def reset_db_state():
    database.db._state._state.set(db_state_default.copy())
    database.db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        database.db.connect()
        yield
    finally:
        if not database.db.is_closed():
            database.db.close()


@router.post("/tag", response_model=schemas.Tag, dependencies=[Depends(get_db)])
async def create_catalog(tag: schemas.TagCreate):
    return crud.create_tag(tag=tag)


@router.get("/tag/{tag_id}", response_model=schemas.Tag, dependencies=[Depends(get_db)])
async def get_tag(tag_id: int):
    return crud.get_tag(tag_id=tag_id)


@router.get("/tags", response_model=schemas.Tag, dependencies=[Depends(get_db)])
async def get_tags(authentication=Header(None), skip: Optional[int] = 0, limit: Optional[int] = 100):
    if not authentication:
        raise exceptions.UnauthorizedHTTPException()
    return crud.get_tags_of_user(user_id=authentication.get("user_id"), skip=skip, limit=limit)


@router.post("/catalog", response_model=schemas.Catalog, dependencies=[Depends(get_db)])
async def create_catalog(catalog: schemas.CatalogCreate):
    return crud.create_catalog(catalog=catalog)


@router.get("/catalog/{catalog_id}", response_model=schemas.Catalog, dependencies=[Depends(get_db)])
async def get_catalog(catalog_id: int):
    return crud.get_catalog(catalog_id=catalog_id)


@router.get("/catalogs", response_model=schemas.Catalog, dependencies=[Depends(get_db)])
async def get_catalogs(authentication=Header(None), skip: Optional[int] = 0, limit: Optional[int] = 100):
    if not authentication:
        raise exceptions.UnauthorizedHTTPException()
    return crud.get_catalogs_of_user(user_id=authentication.get("user_id"), skip=skip, limit=limit)


@router.get("/posts", response_model=schemas.Post, dependencies=[Depends(get_db)])
async def get_posts(authentication=Header(None), skip: Optional[int] = 0, limit: Optional[int] = 100):
    if not authentication:
        raise exceptions.UnauthorizedHTTPException()
    return crud.get_posts_of_user(user_id=authentication.get("user_id"), skip=skip, limit=limit)


@router.post("/post", response_model=schemas.Post, dependencies=[Depends(get_db)])
async def create_post(post: schemas.PostCreate):
    return crud.create_post(post=post)


@router.put("/post/{post_id}", response_model=schemas.Post, dependencies=[Depends(get_db)])
async def update_post(post: schemas.PostUpdate):
    return crud.update_post(post=post)
