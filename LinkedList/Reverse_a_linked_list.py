class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class ReverseALinkedList:

    def __init__(self):
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

    def __reversed__(self):
        pass