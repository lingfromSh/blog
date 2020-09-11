from fastapi import APIRouter, Depends
from sql import schemas, crud, database, models
from sql.database import db_state_default
from core import exceptions

database.db.connect()
database.db.create_tables([models.User, models.Post, models.Catalog, models.Tag, models.PostCatalog, models.PostTag])
database.db.close()

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


@router.put("/", response_model=schemas.User, dependencies=[Depends(get_db)])
async def update_user_self(user: schemas.UserUpdate):
    return crud.update_user(user=user)


@router.get("/{user_id}", response_model=schemas.User, dependencies=[Depends(get_db)])
async def get_user(user_id: int):
    return crud.get_user(user_id=user_id)


@router.post("/login", response_model=schemas.User, dependencies=[Depends(get_db)])
async def login(user: schemas.UserBase):
    db_user = crud.get_user_by_username(username=user.username)
    if db_user and db_user.hashed_password == f"{user.password}not_really_hashed_password":
        return db_user
    raise exceptions.CoreNotFoundHTTPException()


@router.post("/register", response_model=schemas.User, dependencies=[Depends(get_db)])
async def register(user: schemas.UserCreate):
    return crud.create_user(user=user)
