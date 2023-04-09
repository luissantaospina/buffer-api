from app.services.buffer.interface.i_buffer_reader import IBufferReader
from app.data_transfer_objects import MessageDTO


class ReaderFifo(IBufferReader):
    def resolve(self, buffer) -> MessageDTO:
        return buffer.pop(0)
