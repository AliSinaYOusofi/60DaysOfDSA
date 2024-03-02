def two_sum(arr, target):

    first_indice = 0
    second_indices = 0

    for r in arr:
        for v in range(len(arr)):
            if r + arr[v] == target:
                first_indice, second_indices = arr.index(r), v
            else:
                continue
    return first_indice, second_indices


print(two_sum([34, 23, 56, 4], 60))
