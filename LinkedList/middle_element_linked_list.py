import math


def __is_even__(data):
    return int(data) % 2 == 0


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def middle_of_linked_list(self):
        """
        :return: the middle of the linked list, and if even return both of the middle node data
        """
        current_node = self.head
        previous_node = ''
        current_size = (self.__sizeof__() / 2)
        counter = 0

        while counter < current_size:
            counter += 1
            previous_node = current_node
            current_node = current_node.next

        print(counter, current_size)
        if __is_even__(current_size):
            return previous_node.data
        return current_node.data, current_node.next.data

    def __sizeof__(self):
        current_node = self.head
        size = 0

        if self.head is None:
            return size

        while current_node:
            size += 1
            current_node = current_node.next

        return size


linked_middle = LinkedList()
linked_middle.append(22)
linked_middle.append(33)
linked_middle.append(44)
linked_middle.append(55)
linked_middle.append(66)

print(linked_middle.middle_of_linked_list())
