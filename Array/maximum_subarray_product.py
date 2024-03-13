class MaximumProductSubArray:

    def __init__(self, arr):
        self.arr = arr

    def max_sub_array_(self):
        max_product = float('-inf')
        current_product = 1
        starting_index = 0
        ending_index = 0
        temp_starting_index = 0

        for i, num in enumerate(self.arr):
            if current_product * num < num:
                temp_starting_index = i
                current_product = num
            else:
                current_product *= num

            if current_product > max_product:
                max_product = current_product
                starting_index = temp_starting_index
                ending_index = i

        return self.arr[starting_index: ending_index + 1]


data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
lcs = MaximumProductSubArray(data)
print(lcs.max_sub_array_())
