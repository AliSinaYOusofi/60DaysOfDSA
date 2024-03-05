class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class RemoveNNodeAfterMNode:

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

    def remove_nth_node_after_mth_node(self, starting_node_index, how_many_nodes_after):

        size = self.size()

        if how_many_nodes_after > size:
            return
        head = self.head
        starting_node = self.head
        ending_node = self.head
        counter = 1

        while counter < starting_node_index:
            counter += 1
            starting_node = starting_node.next

        counter = 0
        print(starting_node.data, 'starting node is <-')
        while counter <= how_many_nodes_after:
            ending_node = ending_node.next
            counter += 1

        print(ending_node.data, ' ending node <-')
        starting_node.next = ending_node.next

    def view_linked_list(self):
        current = self.head
        print('showing the linked list ->')
        while current:
            print('[+]: {0}'.format(current.data))
            current = current.next

    def size(self):
        counter = 0
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
            counter += 1
        return counter


linked = RemoveNNodeAfterMNode()
linked.append(22)
linked.append(55)
linked.append(66)
linked.append(66)
linked.view_linked_list()
linked.remove_nth_node_after_mth_node(2, 2)
linked.view_linked_list()

