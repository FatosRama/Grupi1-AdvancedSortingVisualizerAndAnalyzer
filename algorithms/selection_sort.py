def selection_sort(arr):
    arr = arr.copy()
    comparisons = 0
    operations = 0
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            comparisons += 1
            yield arr, comparisons, operations

            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        operations += 1
        yield arr, comparisons, operations

    yield arr, comparisons, operations
