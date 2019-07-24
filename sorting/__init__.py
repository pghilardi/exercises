
# Sorting algorithms

# 1: Bubble sort

# bubble sort, time complexity O(n2)
# at the end of each iteration, the last number in the values is guaranteed to be the greater

#########################################################################################################


def bubble(values):
    for i in range(len(values) - 1):
        print(i, '*' * 20)
        for j in range(len(values) - 1 - i):
            print(j)
            if values[j] > values[j + 1]:
                aux = values[j]
                values[j] = values[j + 1]
                values[j + 1] = aux
        print(values)
    print(values)


elements = [5, 4, 3, 2, 1]
bubble(elements)


#########################################################################################################

# 2: quick sort
#
# time complexity O(n2) in the worst case, because it depends of the pivot choose
# on average case is O(n log n)

#########################################################################################################


def quick_sort_partition(array, pivot):
    i = 0  # item from left
    j = len(array) - 2  # item from right
    while i <= j:
        print(i, j)

        if array[i] > array[pivot] > array[j]:
            # swap when the item from left is greater than the pivot and when the item from right is smaller
            # then the pivot
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

        if array[i] < array[pivot]:
            i += 1

        if array[j] > array[pivot]:
            j -= 1

    # swap last item from left with the pivot
    array[i], array[pivot] = array[pivot], array[i]

    # return the array and the new pivot position
    return array, i


def quick_sort_recursive(array):
    if array:
        array, pivot = quick_sort_partition(array, len(array) - 1)
        print('result partition', array, pivot)
        print(array[0:pivot])
        print(array[pivot + 1:])

        array_1 = quick_sort_recursive(array[0:pivot])
        array_2 = quick_sort_recursive(array[pivot + 1:])
        return array_1 + [array[pivot]] + array_2

    return array


def quick_sort(values):
    return quick_sort_recursive(values)


elements = [2, 6, 5, 0, 8, 7, 1, 3]
print(quick_sort(elements))

#########################################################################################################

# 3: merge sort
#
# time complexity O(n2) in the worst case, because it depends of the pivot choose
# on average case is O(n log n)

#########################################################################################################


def merge_sort(values):

    print("Splitting ", values)
    if len(values) > 1:
        mid = len(values) // 2
        left = values[:mid]
        right = values[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                values[k] = left[i]
                i = i + 1
            else:
                values[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            values[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            values[k] = right[j]
            j = j + 1
            k = k + 1

    print("Merging ", values)


elements = [54, 26, 13, 4, 9, 33, 67, 12]
merge_sort(elements)
print(elements)
