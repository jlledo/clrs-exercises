def insertion_sort_recursive(array, index):
    if index == 0:
        return

    insertion_sort_recursive(array, index - 1)

    element = array[index]
    j = index
    while j > 0 and element < array[j - 1]:
        array[j] = array[j - 1]
        j -= 1
    array[j] = element


def insertion_sort(array):
    for i in range(1, len(array)):
        element = array[i]
        j = i
        while i > 0 and element < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = element

    return array


array = [3, 41, 52, 26, 38, 57, 9, 49]
insertion_sort_recursive(array, len(array) - 1)
print(array)
# print(insertion_sort(array))
