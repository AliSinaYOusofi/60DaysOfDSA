class UnionOfSortedArrays:

    def __init__(self, data, second):
        self.arr = data
        self.arr2 = second

    def union(self):
        union_array = []
        for v in self.arr:
            if v not in union_array:
                union_array.append(v)

        for v in self.arr2:
            if v not in union_array:
                union_array.append(v)

        union_array.sort()
        return union_array

    def shorter_way(self):
        union_sorted = set(self.arr) | set(self.arr2)
        return sorted(union_sorted)


uni = UnionOfSortedArrays([1, 2, 3], [4, 5, 6])
print(uni.union())