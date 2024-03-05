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

    def prepend(self, data):

        if not self.head:
            return

        new_node = Node(data)
        head = self.head
        self.head = new_node
        new_node.next = head

    def append_before(self, data, before):

        head = self.head
        before_that_node = ''

        while head.data != before:
            before_that_node = head
            head = head.next

        new_node = Node(data)
        new_node.next = head
        new_node.previous = before_that_node
        before_that_node.next = new_node

    def append_after(self, data, after):

        head = self.head

        while head.data != after and head:

            print(head.data, ' what')
            head = head.next

        new_node = Node(data)
        new_node.next = head.next
        head.next = new_node
        new_node.previous = head

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
linked.prepend(11)
linked.append_before(99, 44)
linked.append_before(100, 99)
linked.append_after(66665, 55)
linked.view_linked_list()
