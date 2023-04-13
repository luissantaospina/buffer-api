from abc import ABC, abstractmethod
from app.data_transfer_objects import PolicyDTO
from app.enums import PolicyEnum
from app.services.buffer.i_buffer.impl import ReaderFifo, ReaderLifo
from app.exceptions import UnsupportedPolicy


class Policy(ABC):
    @abstractmethod
    def reader(self) -> ReaderFifo | ReaderLifo:
        pass


class Fifo(Policy):
    def reader(self) -> ReaderFifo:
        return ReaderFifo()


class Lifo(Policy):
    def reader(self) -> ReaderLifo:
        return ReaderLifo()


class PolicyFactory:
    @staticmethod
    def create_reader(policy: PolicyDTO):
        if policy.method == PolicyEnum.FIFO.value:
            return Fifo().reader()

        elif policy.method == PolicyEnum.LIFO.value:
            return Lifo().reader()

        else:
            raise UnsupportedPolicy('The policy is not supported')
