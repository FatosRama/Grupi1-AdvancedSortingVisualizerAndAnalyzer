def counting_sort(arr):
    arr = arr.copy()
    comparisons = 0
    operations = 0

    if not arr:
        yield arr, comparisons, operations
        return

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1
        operations += 1
        yield arr, comparisons, operations

    idx = 0
    for value, freq in enumerate(count):
        for _ in range(freq):
            arr[idx] = value
            operations += 1
            idx += 1
            yield arr, comparisons, operations

    yield arr, comparisons, operations
