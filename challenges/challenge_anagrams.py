def is_anagram(first_string, second_string):
    first_string_sorted = ''.join(quick_sort(list(first_string.lower())))
    second_string_sorted = ''.join(quick_sort(list(second_string.lower())))
    is_anagram = (False if first_string == '' or second_string == ''
                  else True if first_string_sorted == second_string_sorted
                  else False)
    return (first_string_sorted, second_string_sorted, is_anagram)


def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
    return arr


def partition(arr, start, end):
    pivot = arr[end]
    delimiter = start - 1

    for index in range(start, end):
        if arr[index] <= pivot:
            delimiter = delimiter + 1
            arr[index], arr[delimiter] = arr[delimiter], arr[index]

    arr[delimiter + 1], arr[end] = arr[end], arr[delimiter + 1]

    return delimiter + 1
