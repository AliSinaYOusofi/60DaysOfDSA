class MaxElement:

    def __init__(self, arr):
        self.array = arr

    def find_maximum(self):
        first_element = self.array[0]

        for element in self.array:
            if element >= first_element:
                first_element = element
        return first_element


max_element = MaxElement([3, 34, 23, 1])
print(max_element.find_maximum())
