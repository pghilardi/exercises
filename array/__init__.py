# Array and List algorithms

# 1 Remove duplicated elements from list, keeping order

#########################################################################################################


def remove_duplicted(values):
    unique_values = []
    for value in values:
        if value not in unique_values:
            unique_values.append(value)

    print(unique_values)
    return unique_values


elements = [1, 2, 4, 4, 8, 4, 9, 8, 10, 9]
remove_duplicted(elements)


#########################################################################################################

# 2 kth greatest element
# We can use quick sort here too, so the algorithm can be O(n) on average usage, that is the selection sort

def k_greatest(values, k):
    values = remove_duplicted(values)
    return sorted(values)[len(values) - k]


print(k_greatest(elements, 4))


#########################################################################################################

# 3 get unique values from list

#########################################################################################################


def get_unique(values):
    unique_values = []
    duplicated_values = []
    for value in values:
        if value not in unique_values:
            if value not in duplicated_values:
                unique_values.append(value)
        else:
            unique_values.remove(value)
            duplicated_values.append(value)

    return unique_values


print(elements)
print(get_unique(elements))

#########################################################################################################
