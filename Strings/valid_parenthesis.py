class ValidParenthesis:

    def __init__(self, parenthesis):
        self.parenthesis = parenthesis

    def is_valid_parenthesis(self):
        stack = []
        for par in self.parenthesis:
            if par == '(':
                stack.append(par)
            else:
                stack.pop()
        return not bool(len(stack))


valid_par = ValidParenthesis('(())')
print(valid_par.is_valid_parenthesis())
