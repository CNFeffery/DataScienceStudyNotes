from peewee import SqliteDatabase, Model
from peewee import CharField, FloatField

db = SqliteDatabase('models/sex.db')


class Sex(Model):
    # 地区，唯一
    region = CharField(unique=True)

    # 男性占比
    male = FloatField()

    # 女性占比
    female = FloatField()

    class Meta:
        database = db
        primary_key = False  # 禁止自动生成唯一id列

    @classmethod
    def fetch_all(cls):
        return list(cls.select().dicts())
