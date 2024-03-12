class SumEqualsZero:

    def __init__(self, data):
        self.arr = data

    def subarray_with_sum_equal_zero(self):
        for i in self.arr:
            for j in self.arr:
                if i + j == 0:

                    return [i, j]


sub = SumEqualsZero([1, 2, 3, -3])
print(sub.subarray_with_sum_equal_zero())
