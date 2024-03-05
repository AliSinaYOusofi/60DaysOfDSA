class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class RemoveLastOccurrenceOf:

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

    def remove_last_occurrence_of(self, data):
        if not self.head:
            return

        current_node = self.head
        last_occurrence_of_node = ''
        index_in_chain = 0
        while current_node:

            if current_node.data == data:
                index_in_chain += 1
                last_occurrence_of_node = current_node

            current_node = current_node.next

        if not last_occurrence_of_node:
            print('not found')
            return

        current_node = self.head
        previous_node = ''
        while current_node != last_occurrence_of_node:
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = last_occurrence_of_node.next

    def view_linked_list(self):
        current = self.head
        print('showing the linked list ->')
        while current:
            print('[+]: {0}'.format(current.data))
            current = current.next


last_occurr = RemoveLastOccurrenceOf()
last_occurr.append(22)
last_occurr.append(33)
last_occurr.append(22)
last_occurr.append(25)
last_occurr.view_linked_list()
last_occurr.remove_last_occurrence_of(22)
last_occurr.view_linked_list()