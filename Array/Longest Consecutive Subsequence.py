class LongestConsecutiveSubsequence:

    def __init__(self, data):
        self.arr = data

    def longest_consecutive_sub_sequence(self):
        self.arr.sort()

        return [(x, i) for x, i in enumerate(self.arr)]


log = LongestConsecutiveSubsequence([1, 9, 3, 10, 4, 20, 2])
print(log.longest_consecutive_sub_sequence())
