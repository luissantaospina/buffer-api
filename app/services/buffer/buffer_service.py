from app.services.buffer.readers import BufferReader
from app.data_transfer_objects import MessageDTO, PolicyDTO
from app.factories import PolicyFactory
from app.repositories import \
    insert_item_to_buffer_repository,\
    extract_item_to_buffer_repository,\
    get_all_buffer_repository


def get_all_buffer_service() -> list:
    return get_all_buffer_repository()


def insert_item_to_buffer_service(message_to_insert: MessageDTO) -> MessageDTO:
    return insert_item_to_buffer_repository(message_to_insert)


def extract_item_to_buffer_service(policy: PolicyDTO) -> MessageDTO:
    reader = PolicyFactory().create_reader(policy)
    buffer_reader = BufferReader(reader)
    return extract_item_to_buffer_repository(buffer_reader)
