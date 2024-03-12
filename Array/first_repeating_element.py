class FirstRepeatingElement:

    def __init__(self, arr):
        self.arr = arr

    def first_repeating_element(self):
        return [x for x in self.arr if self.arr.count(x) > 1][0]


first = FirstRepeatingElement([1, 2, 1, 2])
print(first.first_repeating_element())
