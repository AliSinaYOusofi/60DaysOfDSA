class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class RemoveFirstOccurrenceLinkedList:

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

    def remove_first_occurrence_of(self, data):

        current_node = self.head
        previous_node = self.head

        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = current_node.next

    def view_linked_list(self):
        current = self.head
        print('showing the linked list ->')
        while current:
            print('[+]: {0}'.format(current.data))
            current = current.next


linked = RemoveFirstOccurrenceLinkedList()
linked.append(44)
linked.append(55)
linked.append(55)
linked.view_linked_list()
linked.remove_first_occurrence_of(55)
linked.view_linked_list()
