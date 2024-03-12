class Solution:

    def __init__(self, arr, arr1, arr2):
        self.arr = arr
        self.arr1 = arr1
        self.arr2 = arr2

    def common_elements(self):
        return sorted(set(self.arr) & set(self.arr1) & set(self.arr2))


common = Solution([1, 2], [1,5,7], [1, 8, 9])
print(common.common_elements())
