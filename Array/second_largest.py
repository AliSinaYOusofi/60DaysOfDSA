class KthLargest:

    def __init__(self, arr):
        self.arr = arr

    def second_largest(self):
        largest = self.arr[0]
        second_lrg = float('-inf')

        for i in range(1, len(self.arr)):
            if self.arr[i] > largest:
                second_lrg = largest
                largest = self.arr[i]
            elif largest > self.arr[i] > second_lrg:
                second_lrg = self.arr[i]
        return second_lrg


second_largest = KthLargest([34, 23, 45, 37])
print(second_largest.second_largest())
