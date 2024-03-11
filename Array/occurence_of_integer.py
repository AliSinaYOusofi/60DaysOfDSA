class OccurrenceOfElement:

    def __init__(self, data):
        self.arr = data

    def occurrence_of_element(self, element):
        counter = 0
        for ele in self.arr:
            if ele == element:
                counter += 1
        return counter
