"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push("data1")
        self.stack.push("data2")
        self.stack.push("data3")
        self.assertEqual(self.stack.top.data, "data3")
        self.assertEqual(self.stack.top.next_node.data, "data2")
        self.assertEqual(self.stack.top.next_node.next_node.data, "data1")
        self.assertEqual(self.stack.top.next_node.next_node.next_node, None)

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()
        # теперь последний элемента содержит данные data1
        assert stack.top.data == 'data1'
        # данные удаленного элемента
        assert data == 'data2'

    def test_str(self):
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push("data3")
        assert str(self.stack) == "data3 data2 data1"
