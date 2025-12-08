def heap_sort(vis):
    arr = vis.arr
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(vis, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        vis.swap(0, i)
        yield
        yield from heapify(vis, i, 0)

    vis.mark_sorted()
    yield