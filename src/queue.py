class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        result = self.head.data
        self.head = self.head.next_node
        return result

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        queue_string = ''
        while node:
            queue_string += f'{str(node.data)} '
            node = node.next_node
        queue_string = queue_string.strip(' ')

        return queue_string

