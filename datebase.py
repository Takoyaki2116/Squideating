from peewee import *
from flask_login import UserMixin

db = SqliteDatabase('Turtle.db')

class Turtles(UserMixin,Model):
    username = CharField()
    password = CharField()

    class Meta:
        database = db

db.create_tables([Turtles])