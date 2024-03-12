class CyclicallyRotateArrayByOne:

    def __init__(self, arr):
        self.array = arr

    def rotate_array_by_one(self):
        last_element = self.array[len(self.array) - 1]
        rotated_array = [last_element] + self.array[:-1]
        return rotated_array


rotate_by_one = CyclicallyRotateArrayByOne([1, 2, 3, 4, 5])
print(rotate_by_one.rotate_array_by_one())
