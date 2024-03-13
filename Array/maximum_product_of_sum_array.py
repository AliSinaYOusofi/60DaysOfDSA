class MaximumProductOfSubArray:

    def __init__(self, arr):
        self.arr = arr

    def product_of_sub_array(self):
        current_product_result = 1
        current_product = 1

        for element in self.arr:
            current_product = max(element, element * current_product)
            current_product_result = max(current_product_result, current_product)
        return current_product_result


prod = MaximumProductOfSubArray([-1, -3, -10, 0, 60])
print(prod.product_of_sub_array())
