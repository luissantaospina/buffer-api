import unittest
from app.data_transfer_objects import MessageDTO
from app.services.buffer.singleton import Buffer


class TestBuffer(unittest.TestCase):
    def setUp(self):
        self.buffer_instance1 = Buffer()
        self.buffer_instance2 = Buffer()

    def test_singleton(self):
        self.assertIs(self.buffer_instance1, self.buffer_instance2)

    def test_set_get_buffer(self):
        message1 = MessageDTO("test message 1")
        message2 = MessageDTO("test message 2")

        self.buffer_instance1.set_buffer(message1)
        self.buffer_instance2.set_buffer(message2)

        self.assertListEqual(self.buffer_instance1.get_buffer(), [message1, message2])
        self.assertListEqual(self.buffer_instance2.get_buffer(), [message1, message2])
