class RemoveOuterMostParenthesis:

    def __init__(self, string):
        self.string = string

    def remove_outer_most_par(self):
        res, opened = [], 0
        for c in self.string:
            if c == '(' and opened > 0:
                res.append(c)
            if c == ')' and opened > 1:
                res.append(c)
            opened += 1 if c == '(' else -1

        return "".join(res)


outer = RemoveOuterMostParenthesis('()()()')
print(outer.remove_outer_most_par())
