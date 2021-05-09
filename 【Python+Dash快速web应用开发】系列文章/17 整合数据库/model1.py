from peewee import SqliteDatabase, Model
from peewee import CharField, IntegerField, DateTimeField

from datetime import datetime

# 关联数据库，对于sqlite数据库若不存在则会直接创建
db = SqliteDatabase('17 整合数据库/model1.db')


class Model1(Model):
    # 用户名为字符型，并设置唯一性约束
    username = CharField(unique=True)

    # 用户等级设定为整数型
    level = IntegerField()

    # 用户加入时间为时间日期类型
    join_datetime = DateTimeField()

    class Meta:
        database = db  # 指定数据库
        table_name = 'user_info'  # 自定义数据表名，不设置则自动根据类名推导


# 创建数据表，若对应数据库中已存在此表，则会跳过
db.create_tables([Model1])

# 创建单条记录
Model1.create(username='张三', level=6, join_datetime=datetime(2020, 1, 1, 10, 28, 45))

Model1.create(username='李四', level=1, join_datetime=datetime(2020, 5, 1, 10, 28, 45))

# 批量插入数据
(
    Model1
    .insert_many([
        {'username': '王五', 'level': 3, 'join_datetime': datetime(2020, 3, 1, 10, 28, 45)},
        {'username': '赵六', 'level': 2, 'join_datetime': datetime(2020, 4, 1, 10, 28, 45)}
    ])
    .execute()
)

# 删除level小于3的记录
Model1.delete().where(Model1.level < 3).execute()

# 修改username为张三的记录值level字段为8
Model1.update(level=8).where(Model1.username == '张三').execute()

# 获取查询结果方式1：
query_results = Model1.select().where(Model1.level > 2).execute()

for query_result in query_results:
    print(query_result.username)

# 获取查询结果方式2：
query_results = Model1.select().where(Model1.level > 2).dicts()
list(query_results)