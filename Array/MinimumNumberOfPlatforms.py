class MinimumNumberOfPlatforms:

    def __init__(self, arr, dep):
        self.arr = arr
        self.dep = dep

    def minimum_platforms(self):
        arr_sorted, dep_sorted = sorted(self.arr), sorted(self.dep)
        platforms = max_platforms = arr_ptr = dep_ptr = 0

        while arr_ptr < len(self.arr):
            if arr_sorted[arr_ptr] <= dep_sorted[dep_ptr]:
                platforms += 1
                arr_ptr += 1
            else:
                platforms -= 1
                dep_ptr += 1

            max_platforms = max(max_platforms, platforms)

        return max_platforms


mini = MinimumNumberOfPlatforms([100, 300, 500], [900, 400, 600])
print(mini.minimum_platforms())
