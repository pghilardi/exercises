

# Recursion algorithms

# 1: Binary search

#########################################################################################################


def binary_search(array, value, low, high):
    if low > high:
        return None

    middle = (low + high) // 2
    if value < array[middle]:
        return binary_search(array, value, low, middle - 1)
    elif value > array[middle]:
        return binary_search(array, value, middle + 1, high)
    else:
        return middle


values = [1, 7, 12, 23, 39, 52, 80]
print(binary_search(values, 39, 0, 7))


#########################################################################################################


# 2 fibonacci
#
# 0 1 1 2 3 5 8 13 ...

def fibonacci(n):

    if n in [0, 1]:
        return n

    return fibonacci(n - 2) + fibonacci(n - 1)


def optimized_fibonacci(n):
    to_calculate = [0, 1]
    i = 2
    while len(to_calculate) < n:
        v = to_calculate[i - 1] + to_calculate[i - 2]
        to_calculate.append(v)
        i += 1
    print(to_calculate)


print(fibonacci(9))
print(optimized_fibonacci(9))


#########################################################################################################
