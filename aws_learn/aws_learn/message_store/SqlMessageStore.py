from typing import List

from aws_learn.message_store.MessageStore import Message, MessageStore


class SqlMessageStore(MessageStore):
    def __init__(self, connection, table):
        self.connection = connection
        self.table = table

    def write_messages(self, messages: List[Message]):
        pass
