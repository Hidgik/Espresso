from peewee import *
import os

fullname = os.path.join("data", "coffee.db")
db = SqliteDatabase(fullname)


class Person(Model):
    id = IntegerField()
    name = CharField()
    d = CharField()
    gro_gra = CharField()
    name2 = CharField()
    price = IntegerField()
    v = IntegerField()

    class Meta:
        database = db
