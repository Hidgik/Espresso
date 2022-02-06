from peewee import *

db = SqliteDatabase('coffee.db')


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
