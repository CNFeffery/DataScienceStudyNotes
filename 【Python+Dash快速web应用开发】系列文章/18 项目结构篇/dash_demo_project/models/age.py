from peewee import SqliteDatabase, Model
from peewee import CharField, FloatField

db = SqliteDatabase('models/age.db')


class Age(Model):
    # 地区，唯一
    region = CharField(unique=True)

    # 0-14岁占比
    prop_0_to_14 = FloatField()

    # 15-59岁占比
    prop_15_59 = FloatField()

    # 60岁及以上占比
    prop_60_above = FloatField()

    # 65岁及以上占比
    prop_65_above = FloatField()

    class Meta:
        database = db
        primary_key = False  # 禁止自动生成唯一id列

    @classmethod
    def fetch_all(cls):
        return list(cls.select().dicts())
