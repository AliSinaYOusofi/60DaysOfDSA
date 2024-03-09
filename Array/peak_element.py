class PeakElement:

    def __init__(self, arr):
        self.arr = arr

    def peak_element(self):

        if not self.has_length_three():
            return

        elif self.is_sorted_ascending():
            return self.arr[len(self.arr) - 1]

        elif self.is_sorted_descending():
            return self.arr[0]
        return self.peak_element_based_no_neighbors()

    def is_sorted_ascending(self):

        for i in range(len(self.arr) - 1):
            if self.arr[i] > self.arr[i + 1]:
                return False
        return True

    def is_sorted_descending(self):
        for i in range(len(self.arr) - 1):
            if self.arr[i] < self.arr[i + 1]:
                return False
        return False

    def peak_element_based_no_neighbors(self):
        for i in range(len(self.arr) - 1):
            if self.arr[i] < self.arr[i + 1] > self.arr[i + 2]:
                return self.arr[i + 1]
        return 'no peak element'

    def has_length_three(self):
        return len(self.arr) - 1 >= 2


peak = PeakElement([10, 20, 15, 2, 23, 90, 67])
print(peak.peak_element())
print(len([34, 23, 45]))
