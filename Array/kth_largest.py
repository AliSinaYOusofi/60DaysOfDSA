class KthLargest:

    def __init__(self, arr):
        self.arr = arr

    def kth_largest(self, k):
        self.arr.sort()
        return self.arr[k - 1]


kth = KthLargest([34, 23, 45])
print(kth.kth_largest(2))