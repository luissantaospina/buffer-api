from app.data_transfer_objects import PolicyDTO
from app.enums import PolicyEnum
from app.services.buffer.readers import ReaderFifo, ReaderLifo


class Policy:
    def reader(self):
        pass


class Fifo(Policy):
    def reader(self):
        return ReaderFifo()


class Lifo(Policy):
    def reader(self):
        return ReaderLifo()


class PolicyFactory:

    def create_reader(self, policy: PolicyDTO):
        if policy.method == PolicyEnum.FIFO.value:
            return Fifo().reader()

        elif policy.method == PolicyEnum.LIFO.value:
            return Lifo().reader()
