class NoneRepeatingElement:

    def __init__(self, arr):
        self.arr = arr

    def first_none_repeating(self):
        return [x for x in self.arr if self.arr.count(x) == 1][0]


none_repeating = NoneRepeatingElement([1, 2, 3, 2, 3])
print(none_repeating.first_none_repeating())
