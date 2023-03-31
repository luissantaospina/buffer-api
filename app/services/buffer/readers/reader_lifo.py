from app.services.buffer.interface.i_buffer_reader import IBufferReader


class ReaderLifo(IBufferReader):
    def __init__(self) -> None:
        super().__init__()

    def resolve(self, buffer) -> None:
        buffer.pop()
