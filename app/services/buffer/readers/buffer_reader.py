from app.services.buffer.i_buffer.i_buffer_reader import IBufferReader
from app.data_transfer_objects import MessageDTO


class BufferReader:
    __reader = None

    def __init__(self, reader: IBufferReader) -> None:
        self.__reader = reader
        super().__init__()

    def reader(self, buffer) -> MessageDTO:
        return self.__reader.resolve(buffer)
