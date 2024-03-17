class GenerateParenthesis:

    def __init__(self, times):
        self.times = times
        self.combos = []

    def generate_parenthesis_combinations(self):
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * self.times:
                self.combos.append(s)
                return
            if left < self.times:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack()
        return self.combos


par = GenerateParenthesis(3)
print(par.generate_parenthesis_combinations())
