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

    def largest_node(self):
        if not self.head:
            return
        largest = self.head.data
        head = self.head

        while head:
            if largest <= head.data:
                largest = head.data
            head = head.next

        return largest

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
print(linked.largest_node())
linked.view_linked_list()
