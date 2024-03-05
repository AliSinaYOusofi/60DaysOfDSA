import math


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class RemoveFromTheMiddle:

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

    def size(self):
        counter = 0
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
            counter += 1
        return counter

    def remove_the_middle_node(self):

        middle_node = math.floor(self.size() / 2)

        current_node = self.head
        previous_node = ''
        counter = 0

        while counter <= middle_node:
            previous_node = current_node
            current_node = current_node.next
            counter += 1

        if previous_node:
            previous_node.next = current_node.next

    def view_linked_list(self):
        current = self.head
        print('showing the linked list ->')
        while current:
            print('[+]: {0}'.format(current.data))
            current = current.next


linked_ = RemoveFromTheMiddle()
linked_.append(22)
linked_.append(44)
linked_.append(22)
linked_.append(422)
linked_.view_linked_list()
linked_.remove_the_middle_node()
linked_.view_linked_list()
