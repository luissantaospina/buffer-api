from app.services.buffer.singleton import Buffer
from app.data_transfer_objects import MessageDTO, PolicyDTO
from app.services.buffer.buffer_service import \
    get_all_buffer_service,\
    insert_item_to_buffer_service,\
    extract_item_to_buffer_service


def get_all_buffer() -> Buffer:
    return get_all_buffer_service()


def insert_item_to_buffer(message_to_insert: MessageDTO) -> MessageDTO:
    return insert_item_to_buffer_service(message_to_insert)


def extract_item_to_buffer(policy: PolicyDTO) -> None:
    extract_item_to_buffer_service(policy)
