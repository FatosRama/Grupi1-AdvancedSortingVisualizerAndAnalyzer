def quick_sort(arr):
    comparisons = 0
    swaps = 0
    arr = arr.copy()

    def sort(l, r):
        nonlocal comparisons, swaps

        if l >= r:
            return

        pivot = arr[(l + r) // 2]
        i, j = l, r

        while i <= j:
            while arr[i] < pivot:
                comparisons += 1
                i += 1
                yield arr, comparisons, swaps

            while arr[j] > pivot:
                comparisons += 1
                j -= 1
                yield arr, comparisons, swaps

            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
                yield arr, comparisons, swaps
                i += 1
                j -= 1

        yield from sort(l, j)
        yield from sort(i, r)

    yield from sort(0, len(arr) - 1)
    yield arr, comparisons, swaps
