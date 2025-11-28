def insertion_sort(arr):
    """
    Insertion Sort Algorithm.
    Params:
        arr (list[int]): Input list of integers
    Returns:
        tuple: (sorted_list, comparisons, operations)
    Note:
        Track comparisons and operations (shifts + placements) for visualization and analysis.
    """
    comparisons = 0
    operations = 0
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                operations += 1
                j -= 1
            else:
                break

        arr[j + 1] = key
        operations += 1

    return arr, comparisons, operations
