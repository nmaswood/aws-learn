from abc import ABC, abstractmethod
from typing import TypedDict, List


class Message(TypedDict):
    message_id: str
    attr: str


class MessageStore(ABC):
    @abstractmethod
    def write_messages(self, messages: List[Message]):
        pass

    def write_message(self, message: Message):
        return self.write_messages(list(message))
