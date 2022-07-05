from peewee import SqliteDatabase, Model

sqlite_db = SqliteDatabase(':memory:', pragmas={'journal_mode': 'wal'})


class BaseModel(Model):
    class Meta:
        database = sqlite_db
