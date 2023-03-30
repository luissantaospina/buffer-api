from app.services.buffer import Buffer
from app.services.buffer_reader import BufferReader
from app.services.reader_fifo import ReaderFifo
from app.services.reader_lifo import ReaderLifo


def get_all_buffer():
    current_buffer = Buffer().get_buffer()
    return current_buffer


def insert_item_to_buffer(message_to_insert) -> None:
    current_buffer = Buffer()
    current_buffer.set_buffer(message_to_insert)


def extract_item_to_buffer(policy) -> None:
    current_buffer = Buffer().get_buffer()
    if policy == 'FIFO':
        buffer_reader = BufferReader(ReaderFifo())
        buffer_reader.reader(current_buffer)
    else:
        buffer_reader = BufferReader(ReaderLifo())
        buffer_reader.reader(current_buffer)
