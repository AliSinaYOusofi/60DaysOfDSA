class LongestConsecutiveSubsequence:

    def __init__(self, data):
        self.arr = data

    def longest_consecutive_sub_sequence(self):

        self.arr.sort()
        ending_index = 0
        counter = self.arr[0] - 1

        for element in self.arr:

            if element == counter + 1:
                ending_index += 1
                counter = element

        return self.arr[:ending_index]


log = LongestConsecutiveSubsequence([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42])
print(log.longest_consecutive_sub_sequence())
