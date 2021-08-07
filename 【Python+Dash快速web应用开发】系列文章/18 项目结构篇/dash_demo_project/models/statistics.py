from peewee import SqliteDatabase, Model
from peewee import CharField, FloatField, IntegerField

db = SqliteDatabase('models/statistics.db')


class Statistics(Model):
    # 地区，唯一
    region = CharField(unique=True)

    # 2020普查人口数量
    pop_2020 = IntegerField()

    # 2020人口全国占比
    prop_2020 = FloatField()

    # 2010人口全国占比
    prop_2010 = FloatField()

    class Meta:
        database = db
        primary_key = False  # 禁止自动生成唯一id列

    @classmethod
    def fetch_all(cls):
        return list(cls.select().dicts())
