from peewee import SqliteDatabase, Model
from peewee import CharField, DateTimeField, TextField
from datetime import datetime

db = SqliteDatabase('message_board.db')


class MessageBoard(Model):
    nickname = CharField()

    pub_datetime = DateTimeField()

    message_content = TextField()

    class Meta:
        database = db  # 指定数据库
        table_name = 'message_board'  # 自定义数据表名，不设置则自动根据类名推导


db.create_tables([MessageBoard])


# 新增留言记录
def submit_new_message(nickname, message_content):
    MessageBoard.create(
        nickname=nickname,
        pub_datetime=datetime.now(),
        message_content=message_content
    )


# 获取全部留言记录
def fetch_all_message():
    return list(MessageBoard.select().dicts())
