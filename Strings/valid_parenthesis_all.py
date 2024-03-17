class AllParenthesisCombinationIsValid:

    def __init__(self, parenthesis):
        self.parenthesis = parenthesis
        self.stack = []

    def is_combination_valid_parenthesis(self):
        for par in self.parenthesis:
            if par == '(' or par == '[' or par == '{':
                self.stack.append(par)
            else:
                if not self.stack:
                    return False
                current_par = self.stack.pop()
                if current_par == '}':
                    self.stack.pop(self.stack.index('}'))
                elif current_par == ']':
                    self.stack.pop(self.stack.index(']'))
                elif current_par == ')':
                    self.stack.pop(self.stack.index(')'))
        return not len(self.stack)


comb = AllParenthesisCombinationIsValid('(){}[]')
print(comb.is_combination_valid_parenthesis())
