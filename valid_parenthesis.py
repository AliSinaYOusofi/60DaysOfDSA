class Stack:

    stack = []
    index = 0
    parenthesis = ''

    def __init__(self, parenthesis):
        self.stack = []
        self.parenthesis = parenthesis
        self.index = 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def last(self):
        return self.parenthesis[len(self.parenthesis) - 1]

    def is_parenthesis_valid(self):
        pass


valid_parenthesis = Stack('(])')
print(valid_parenthesis.is_parenthesis_valid())
