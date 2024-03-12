class AlternativeNegativeAndPositives:

    def __init__(self, arr):
        self.arr = arr

    def alternative_negative_and_positive(self):

        positives = [x for x in self.arr if x >= 0]
        negatives = [y for y in self.arr if y < 0]

        alternative_arr = []

        positive_counter, negative_counter = 0, 0

        while positive_counter < len(positives) and negative_counter < len(negatives):
            alternative_arr.append(positives[positive_counter])
            alternative_arr.append(negatives[negative_counter])
            positive_counter += 1
            negative_counter += 1

        while positive_counter < len(positives):
            alternative_arr.append(positives[positive_counter])
            positive_counter += 1

        while negative_counter < len(negatives):
            alternative_arr.append(negatives[negative_counter])
            negative_counter += 1

        return alternative_arr


alternate = AlternativeNegativeAndPositives([1, 2, 3, -3, -2, -5, -4])
print(alternate.alternative_negative_and_positive())
