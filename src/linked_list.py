class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next_node = None
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        current_node = self.head

        while current_node.next_node:
            current_node = current_node.next_node

        current_node.next_node = new_node
        new_node.next_node = None

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        """Возвращает список с данными, содержащимися в односвязном списке LinkedList"""
        data_list = []
        current_node = self.head

        while current_node.next_node:
            data_list.append(current_node.data)
            current_node = current_node.next_node
        data_list.append(current_node.data)
        return data_list

    def get_data_by_id(self, id_value):
        """Возвращает первый найденный в LinkedList словарь с ключом 'id',
        значение которого равно переданному в метод значению"""

        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
            try:
                if current_node.data['id'] == id_value:
                    return current_node.data
            except TypeError:
                print("Данные не являются словарем или в словаре нет id")
