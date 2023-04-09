from abc import ABC, abstractmethod
from app.data_transfer_objects import MessageDTO


class IBufferReader(ABC):
    @abstractmethod
    def resolve(self, buffer) -> MessageDTO:
        pass
