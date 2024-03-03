class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, data):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node:
            current_node = current_node.next

        current_node.next = new_node

    def middle_of_linked_list(self):

        current_node = self.head
        current_size = self.__sizeof__() / 2
        counter = 0

        while current_node and counter < current_size:
            counter += 1
            current_node = current_node.next

        return current_node.data


    def __sizeof__(self):
        current_node = self.head
        size = 0

        if self.head is None:
            return size

        while current_node:
            size += 1
            current_node = current_node.next

        return size