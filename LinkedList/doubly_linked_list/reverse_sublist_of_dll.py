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
        if end < start or not self.head:
            return

        current_node = self.head
        previous_node = None
        counter = 1

        # Move current_node to the start position
        while counter < start and current_node:
            previous_node = current_node
            current_node = current_node.next
            counter += 1

        if not current_node:
            return

        # Save the node before the sublist to reconnect later
        before_starting_node = previous_node

        # Reverse the sublist
        sublist_head = current_node
        sublist_previous = None

        while counter <= end and current_node:
            next_node = current_node.next
            current_node.next = sublist_previous
            sublist_previous = current_node
            current_node = next_node
            counter += 1

        # Reconnect the reversed sublist
        sublist_head.next = current_node

        if before_starting_node:
            before_starting_node.next = sublist_previous
        else:
            # Update the head if the sublist starts from the beginning
            self.head = sublist_previous

    def view_linked_list(self):
        current = self.head
        print('showing the linked list ->')
        while current:
            print('[+]: Next => {0}'.format(current.data))
            current = current.next


linked = DLL()
linked.append('2asss')
linked.append('2b')
linked.append('2c')
linked.append('2b')
linked.append('2aa')
linked.append('2cs')
linked.view_linked_list()
linked.reverse_a_subset_of_dll(2, 5)
linked.view_linked_list()
