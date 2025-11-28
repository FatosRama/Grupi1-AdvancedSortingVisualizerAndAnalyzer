def insertion_sort(arr):
    """
    Insertion Sort Algorithm.
    Params:
        arr (list[int]): Input list of integers
    Returns:
        tuple: (sorted_list, comparisons, shifts)
    Note:
        Track comparisons and shifts.
    """
    comparisons = 0
    shifts = 0
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key
        shifts += 1

    return arr, comparisons, shifts
