from peewee import SqliteDatabase, Model, TextField, ForeignKeyField, DateField
import datetime

db = SqliteDatabase('sqlite.db')


class DB(Model):
    class Meta:
        database = db


class Update(DB):
    date = DateField(default=datetime.date.today)


class Anime(DB):
    title = TextField(default="Без названия")
    url = TextField(default="Без ссылки")
    update = ForeignKeyField(Update, backref='updates')


db.connect()
db.create_tables([Update, Anime], safe=True)
db.close()
