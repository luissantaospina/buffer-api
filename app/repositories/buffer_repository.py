from app.data_transfer_objects import MessageDTO
from flask import json
from app.services.buffer.readers import BufferReader
from app.exceptions import EmptyBuffer, FailCache
from app.cache import redis_cache
import redis


def get_all_buffer_repository() -> list:
    try:
        cached_buffer = redis_cache.get('buffer')
        if cached_buffer is None:
            cached_buffer = []
        else:
            cached_buffer = json.loads(cached_buffer.decode('utf-8'))
        return cached_buffer
    except redis.exceptions.ConnectionError as ex:
        raise FailCache(ex)


def insert_item_to_buffer_repository(message_to_insert: MessageDTO) -> MessageDTO:
    try:
        cached_buffer = get_all_buffer_repository()
        cached_buffer.append(message_to_insert.body)
        redis_cache.set('buffer', json.dumps(cached_buffer))
        return message_to_insert
    except redis.exceptions.ConnectionError as ex:
        raise FailCache(ex)


def extract_item_to_buffer_repository(buffer_reader: BufferReader) -> MessageDTO:
    try:
        cached_buffer = get_all_buffer_repository()
        item_extracted = buffer_reader.reader(cached_buffer)
        redis_cache.set('buffer', json.dumps(cached_buffer))
        return item_extracted
    except:
        raise EmptyBuffer('The buffer is currently empty')
