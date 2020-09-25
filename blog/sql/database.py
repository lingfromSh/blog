from contextvars import ContextVar

import peewee
from datetime import datetime
from conf import settings


DATABASE_TYPE = settings.DATABASE_SETTINGS["type"]
DATABASE_NAME = settings.DATABASE_SETTINGS["url"]
db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


database_class_mapping = {
    "sqlite": peewee.SqliteDatabase,
    "postgres": peewee.PostgresqlDatabase,
    "mysql": peewee.MySQLDatabase,
}

db = database_class_mapping[DATABASE_TYPE](DATABASE_NAME, check_same_thread=False)

db._state = PeeweeConnectionState()


class Model(peewee.Model):
    id = peewee.AutoField(primary_key=True)

    created = peewee.DateTimeField(default=datetime.utcnow)
    updated = peewee.DateTimeField(default=datetime.utcnow)

    class Meta:
        database = db
