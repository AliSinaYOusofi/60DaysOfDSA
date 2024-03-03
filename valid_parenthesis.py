class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def is_parenthesis_valid(self, parenthesis):
        opening_brackets = ['(', '{', '[']
        closing_brackets = [')', '}', ']']

        for par in parenthesis:
            if par in opening_brackets:
                self.push(par)
            elif par in closing_brackets:
                if self.is_empty() or opening_brackets.index(self.pop()) != closing_brackets.index(par):
                    return False

        return self.is_empty()


valid_parenthesis = Stack()
print(valid_parenthesis.is_parenthesis_valid('()'))
