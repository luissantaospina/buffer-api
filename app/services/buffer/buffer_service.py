from app.services.buffer.singleton import Buffer
from app.services.buffer.readers import BufferReader
from app.data_transfer_objects import MessageDTO, PolicyDTO
from app.factories import PolicyFactory


def get_all_buffer_service() -> Buffer:
    current_buffer = Buffer().get_buffer()
    return current_buffer


def insert_item_to_buffer_service(message_to_insert: MessageDTO) -> MessageDTO:
    current_buffer = Buffer()
    return current_buffer.set_buffer(message_to_insert.body)


def extract_item_to_buffer_service(policy: PolicyDTO) -> MessageDTO | str:
    current_buffer = Buffer().get_buffer()
    if current_buffer:
        reader = PolicyFactory().create_reader(policy)
        buffer_reader = BufferReader(reader)
        return buffer_reader.reader(current_buffer)
    else:
        return ''
