class SortZerosOnesAndTwos:

    def __init__(self, data):
        self.arr = data

    def sort_zero_one_twos(self):

        low = 0
        mid = 0
        high = len(self.arr) - 1

        while mid <= high:

            if self.arr[mid] == 0:
                self.arr[low], self.arr[mid] = self.arr[mid], self.arr[low]
                mid += 1
                low += 1
            elif self.arr[mid] == 1:
                mid += 1
            else:
                self.arr[mid], self.arr[high] = self.arr[high], self.arr[mid]
                high -= 1
        return self.arr


sort = SortZerosOnesAndTwos([0, 0, 0, 2, 2, 1])
print(sort.sort_zero_one_twos())
