class NegativesToOneSide:

    def __init__(self, data):
        self.arr = data

    def negative_on_one_side(self):

        self.arr.sort()
        return self.arr


sor = NegativesToOneSide([34, 23, 45, -3, 4])
print(sor.negative_on_one_side())