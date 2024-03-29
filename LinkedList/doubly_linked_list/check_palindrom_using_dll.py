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

    def straight(self):
        current_node = self.head
        text = ''

        while current_node:
            text += current_node.data
            current_node = current_node.next

        return text

    @staticmethod
    def reversed_text(text):
        return ''.join(list(text)[::-1])

    def is_palindrome(self):
        straight_text = self.straight()
        reversed_text = self.reversed_text(straight_text)
        return straight_text == reversed_text

    def view_linked_list(self):
        current = self.head
        print('showing the linked list ->')
        while current:
            print('[+]: Next => {0}'.format(current.data))
            current = current.next


linked = DLL()
linked.append('m')
linked.append('o')
linked.append('o')
linked.append('m')
linked.view_linked_list()
print(linked.is_palindrome())
