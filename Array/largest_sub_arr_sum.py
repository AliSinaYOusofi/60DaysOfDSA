
class LargestContiguousSum:

    def __init__(self, data):
        self.arr = data

    def kad_algo(self):
        current_sum = 0
        max_sum = float('-inf')

        for element in self.arr:
            current_sum = max(element, element + current_sum)
            max_sum = max(max_sum, current_sum)
        return max_sum


data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
lcs = LargestContiguousSum(data)
print(lcs.kad_algo())
