class FindDuplicates:

    def __init__(self, arr):
        self.arr = arr

    def find_duplicates(self):
        return [x for x, i in enumerate(self.arr) if self.arr.count(x) > 1]


dups = FindDuplicates([1, 2, 3, 4, 2, 4])
print(dups.find_duplicates())
