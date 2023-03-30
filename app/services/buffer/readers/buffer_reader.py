from app.services.buffer.i_buffer_reader import IBufferReader


class BufferReader():
    __reader = None

    def __init__(self, reader: IBufferReader) -> None:
        self.__reader = reader
        super().__init__()

    def reader(self, buffer):
        self.__reader.resolve(buffer)
