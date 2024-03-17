class Solution:

    def __init__(self, data):
        self.arr = data

    def maximum_sum_of_all_rotations(self):
        # rotate on every iteration
        # and sum by mul i * self.arr[i]
        sums = []

        for i in range(len(self.arr)):
            # rotate the arr
            rotated_arr = [self.arr[-1]] + self.arr[:-1]
            self.arr = rotated_arr
            row_sum = sum([index * value for index, value in enumerate(self.arr)])
            sums.append(row_sum)

        return max(sums)


rotation = Solution([8, 3, 1, 2])
print(rotation.maximum_sum_of_all_rotations())