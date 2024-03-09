class SecondSmallest:

    def __init__(self, arr):
        self.arr = arr

    def second_smallest(self):
        smallest = self.arr[0]
        second_small_element = float('inf')

        for i in range(1, len(self.arr)):
            if self.arr[i] < smallest:
                second_small_element = smallest
                smallest = self.arr[i]
            elif smallest < self.arr[i] < second_small_element:
                second_small_element = self.arr[i]
        return second_small_element


second_smallest = SecondSmallest([1, 2, 3, 56, 34, 23])
print(second_smallest.second_smallest())