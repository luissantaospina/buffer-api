from app.services.buffer.interface.i_buffer_reader import IBufferReader


class BufferReader:
    __reader = None

    def __init__(self, reader: IBufferReader) -> None:
        self.__reader = reader
        super().__init__()

    def reader(self, buffer) -> None:
        self.__reader.resolve(buffer)
