class ScoreOfParenthesis:

    def __init__(self, string):
        self.string = string
        self.score = [0]

    def score_of_parenthesis(self):
        for par in self.string:

            if par == '(':
                self.score.append(0)

            else:
                score = self.score.pop()

                if score == 0:

                    self.score[-1] += 1
                else:
                    self.score[-1] += 2 * score
        return self.score[0]


score = ScoreOfParenthesis('(()(()))')
print(score.score_of_parenthesis())
