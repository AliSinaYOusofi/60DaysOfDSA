class SubArraySum:

    def __init__(self, data):
        self.arr = data

    def sub_array_sum(self, total):
        sub_sum = 0
        starting_index = 0
        lasting_index = 0

        for i in range(len(self.arr) - 1):
            starting_index += 1
            for v in range(i + 1, len(self.arr)):
                sub_sum += self.arr[v]
                lasting_index += 1

            sub_sum += self.arr[i]
            if sub_sum == total:
                break
            else:
                sub_sum = 0
        return sub_sum, lasting_index - 1, starting_index - 1


sub_sm = SubArraySum([1, 2, 3, 4])
print(sub_sm.sub_array_sum(9))
