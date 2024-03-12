class MissingElement:

    def __init__(self, arr):
        self.arr = arr

    def missing_integer(self):
        counter = 1
        for element in self.arr:
            if element != counter:
                break
            counter += 1
        return counter


missing = MissingElement([1, 3])
print(missing.missing_integer())
