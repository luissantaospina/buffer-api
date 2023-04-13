import unittest
import redis
from app.data_transfer_objects import MessageDTO
from app.services.buffer.i_buffer.impl import ReaderFifo
from app.services.buffer.readers import BufferReader
from app.repositories.buffer_repository import \
    get_all_buffer_repository,\
    insert_item_to_buffer_repository,\
    extract_item_to_buffer_repository


class TestBuffer(unittest.TestCase):
    def setUp(self):
        redis_cache = redis.Redis(host='localhost', port=6379, db=0)
        redis_cache.flushall()

    def test_insert_item_to_buffer_repository(self):
        message_to_insert = MessageDTO(body=1)
        result = insert_item_to_buffer_repository(message_to_insert)
        self.assertEqual(result.body, 1)

    def test_get_all_buffer_repository(self):
        cached_buffer = get_all_buffer_repository()
        self.assertEqual(cached_buffer, [])

        message_to_insert = MessageDTO(body=1)
        insert_item_to_buffer_repository(message_to_insert)

        cached_buffer = get_all_buffer_repository()
        self.assertEqual(cached_buffer, [1])

    def test_extract_item_to_buffer_repository(self):
        message_to_insert = MessageDTO(body=1)
        insert_item_to_buffer_repository(message_to_insert)

        buffer_reader = BufferReader(ReaderFifo())
        item_extracted = extract_item_to_buffer_repository(buffer_reader)
        self.assertEqual(item_extracted, 1)

        cached_buffer = get_all_buffer_repository()
        self.assertEqual(cached_buffer, [])
