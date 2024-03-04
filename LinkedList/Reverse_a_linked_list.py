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

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def reverse(self):

        prev_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

    def view_linked_list(self):
        current = self.head

        while current:
            print('[+]: {0}'.format(current.data))
            current = current.next


linked_list = ReverseALinkedList()
linked_list.append(3)
linked_list.append(4)
linked_list.view_linked_list()
linked_list.reverse()
linked_list.view_linked_list()
