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

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_a_node(self, data):
        current_node = self.head

        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None

        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = current_node.next
        current_node = None

    def view_linked_list(self):
        current = self.head

        while current:
            print('[+]: {0}'.format(current.data))
            current = current.next


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)
linked_list.append(55)
linked_list.view_linked_list()
linked_list.delete_a_node(1)
linked_list.view_linked_list()
