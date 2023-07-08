import unittest

from src.queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual(self.queue.head.data, "data1")
        self.assertEqual(self.queue.head.next_node.data, "data2")
        self.assertEqual(self.queue.tail.data, "data3")
        self.assertEqual(self.queue.tail.next_node, None)

    def test_str(self):
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        assert str(self.queue) == "data1 data2 data3"

    def test_dequeue(self):
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        assert self.queue.dequeue() == 'data1'
        assert self.queue.dequeue() == 'data2'
        assert self.queue.dequeue() == 'data3'
        assert self.queue.dequeue() is None
