class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self) -> str:
        """Вывод данных стека в строковом представлении"""
        node = self.top
        if node is None:
            return str(None)

        stack_string = ''
        while node:
            stack_string += f'{str(node.data)} '
            node = node.next_node
        stack_string = stack_string.strip(' ')
        return stack_string

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data)
        if self.top:
            new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        result = self.top.data
        self.top = self.top.next_node
        return result
