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

    def view_linked_list(self):
        current = self.head
        print('showing the linked list ->')
        while current:
            print('[+]: Next => {0}'.format(current.data))
            current = current.next


linked = DLL()
linked.append(22)
linked.append(44)
linked.append(55)
linked.append(6665)
linked.view_linked_list()
