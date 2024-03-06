class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        new_node.previous = current_node

    def reverse_a_subset_of_dll(self, start, end):
        pass

    def view_linked_list(self):
        current = self.head
        print('showing the linked list ->')
        while current:
            print('[+]: Next => {0}'.format(current.data))
            current = current.next


linked = DLL()
linked.append('2a')
linked.append('2b')
linked.append('2c')
linked.append('2b')
linked.append('2a')
linked.append('2c')
linked.view_linked_list()
linked.view_linked_list()
