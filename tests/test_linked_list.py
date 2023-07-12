import unittest

from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_and_str(self):
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})
        assert str(self.ll) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"

    def test_to_list(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        lst = self.ll.to_list()
        assert lst == [{'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'}]

    def test_get_data_by_id(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        user_data = self.ll.get_data_by_id(3)
        assert user_data == {'id': 3, 'username': 'mosh_s'}
