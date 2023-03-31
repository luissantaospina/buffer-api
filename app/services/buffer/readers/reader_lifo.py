from app.services.buffer.interface.i_buffer_reader import IBufferReader
from app.data_transfer_objects import MessageDTO


class ReaderLifo(IBufferReader):
    def __init__(self) -> None:
        super().__init__()

    def resolve(self, buffer) -> MessageDTO:
        return buffer.pop()
