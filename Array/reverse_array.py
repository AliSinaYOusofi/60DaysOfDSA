class ReverseArray:

    def __init__(self, arr):
        self.array = arr

    def reverse_array(self):
        rev = []
        for i in range(len(self.array), 0, -1):
            rev.append(self.array[i - 1])

        return rev


reversed_arr = ReverseArray([1, 2, 7, 345, 23, 4, 123, 6])
print(reversed_arr.reverse_array())
