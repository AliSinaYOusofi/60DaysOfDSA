class IntersectionOfTwoSortedArray:

    def __init__(self, first_array, second_array):
        self.first_array = first_array
        self.second_array = second_array

    def intersection_shortest_way(self):
        intersection = set(self.first_array) & set(self.second_array)
        return sorted(intersection)


so = IntersectionOfTwoSortedArray([1, 2, 3], [2])
print(so.intersection_shortest_way())
