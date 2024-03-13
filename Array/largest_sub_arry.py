class LargestContiguousSum:

    def __init__(self, arr):
        self.arr = arr

    def kad_algo(self):
        max_sum = float('-inf')
        current_sum = 0
        start_index = 0
        end_index = 0
        temp_start_index = 0

        for i, num in enumerate(self.arr):

            if current_sum + num < num:
                temp_start_index = i
                current_sum = num
            else:
                current_sum += num

            if current_sum > max_sum:
                max_sum = current_sum
                start_index = temp_start_index
                end_index = i

        return self.arr[start_index:end_index + 1]


data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
lcs = LargestContiguousSum(data)
print(lcs.kad_algo())
