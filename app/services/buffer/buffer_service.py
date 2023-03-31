from app.services.buffer.singleton import Buffer
from app.services.buffer.readers import BufferReader
from app.data_transfer_objects import MessageDTO, PolicyDTO
from app.factories import PolicyFactory


def get_all_buffer() -> Buffer:
    current_buffer = Buffer().get_buffer()
    return current_buffer


def insert_item_to_buffer(message_to_insert: MessageDTO) -> None:
    current_buffer = Buffer()
    current_buffer.set_buffer(message_to_insert.body)


def extract_item_to_buffer(policy: PolicyDTO) -> None:
    current_buffer = Buffer().get_buffer()
    if current_buffer:
        reader = PolicyFactory().create_reader(policy)
        buffer_reader = BufferReader(reader)
        buffer_reader.reader(current_buffer)
