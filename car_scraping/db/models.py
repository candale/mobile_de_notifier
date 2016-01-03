import datetime

from peewee import Model, FixedCharField, ForeignKeyField, DateTimeField
from playhouse.sqlite_ext import SqliteExtDatabase

from car_scraping import settings

db = SqliteExtDatabase(settings.DATABSE_FILE)


class BaseModel(Model):
    class Meta:
        database = db


class Car(BaseModel):

    url = FixedCharField(max_length=1024, unique=True)
    title = FixedCharField(max_length=524)
    price = FixedCharField(max_length=256)
    seller_info = FixedCharField(max_length=1024)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        order_by = ('-created_at',)


class Photo(BaseModel):
    car = ForeignKeyField(Car, 'car')
    url = FixedCharField(max_length=1024)
