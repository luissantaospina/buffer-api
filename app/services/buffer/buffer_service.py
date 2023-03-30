from app.services.buffer.buffer import Buffer
from app.services.buffer.readers.buffer_reader import BufferReader
from app.services.buffer.readers import ReaderFifo, ReaderLifo
from app.data_transfer_objects import MessageDTO, PolicyDTO
from app.enums import PolicyEnum


def get_all_buffer() -> Buffer:
    current_buffer = Buffer().get_buffer()
    return current_buffer


def insert_item_to_buffer(message_to_insert: MessageDTO) -> None:
    current_buffer = Buffer()
    current_buffer.set_buffer(message_to_insert.body)


def extract_item_to_buffer(policy: PolicyDTO) -> None:
    current_buffer = Buffer().get_buffer()
    if policy.method == PolicyEnum.FIFO.value and current_buffer:
        buffer_reader = BufferReader(ReaderFifo())
        buffer_reader.reader(current_buffer)
    if policy.method == PolicyEnum.LIFO.value and current_buffer:
        buffer_reader = BufferReader(ReaderLifo())
        buffer_reader.reader(current_buffer)
