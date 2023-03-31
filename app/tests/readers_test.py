import unittest
from app.services.buffer.readers import ReaderFifo, ReaderLifo


class TestReader(unittest.TestCase):
    def test_resolve_removes_first_item_from_buffer_fifo(self):
        reader = ReaderFifo()
        buffer_test = [1, 2, 3, 4, 5]
        reader.resolve(buffer_test)
        self.assertEqual(buffer_test, [2, 3, 4, 5])

    def test_resolve_removes_first_item_from_buffer_lifo(self):
        reader = ReaderLifo()
        buffer_test = [1, 2, 3, 4, 5]
        reader.resolve(buffer_test)

        self.assertEqual(buffer_test, [1, 2, 3, 4])
