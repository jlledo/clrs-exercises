from math import floor


def binary_search(array, value):
    lo = 0
    hi = len(array)

    # While endpoints don't overlap
    while lo <= hi:
        mid = floor((lo + hi) / 2)
        # lo becomes mid + 1 if array[mid] < value
        # hi becomes mid - 1 if array[mid] > value
        if array[mid] < value:
            lo = mid + 1
        elif array[mid] > value:
            hi = mid - 1
        else:
            return mid

    return None


def binary_search_recursive(array, value):
    return _binary_search_recursive_internal(array, value, 0, len(array))


def _binary_search_recursive_internal(array, value, lo, hi):
    # If endpoints don't overlap
    if lo > hi:
        return None

    mid = floor((lo + hi) / 2)
    # lo becomes mid + 1 if array[mid] < value
    # hi becomes mid - 1 if array[mid] > value
    if array[mid] < value:
        lo = mid + 1
    elif array[mid] > value:
        hi = mid - 1
    else:
        return mid

    return _binary_search_recursive_internal(array, value, lo, hi)


array = [3, 9, 26, 38, 41, 49, 52, 57]
print(binary_search(array, 9))
print(binary_search_recursive(array, 9))
