class MinimumElement:

    def __init__(self, arr):
        self.array = arr

    def find_minimum(self):
        first_element = self.array[0]

        for element in self.array:
            if first_element >= element:
                first_element = element
        return first_element


mini = MinimumElement([2, 3, 5, 6, 1])
print(mini.find_minimum())