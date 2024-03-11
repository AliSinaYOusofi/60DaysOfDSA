class KthSmallest:

    def __init__(self, data):
        self.arr = data

    def kth_smallest(self, k):
        self.arr.sort()
        self.arr.reverse()
        return self.arr[k - 1]


kth = KthSmallest([23, 45, 23, 12, 56])
print(kth.kth_smallest(4))
