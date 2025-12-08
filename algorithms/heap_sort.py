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


    def heapify(vis, n, i):
        arr = vis.arr
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            vis.compare(left, largest)
            yield
            if arr[left] > arr[largest]:
                largest = left

                if right < n:
                    vis.compare(right, largest)
                    yield
                    if arr[right] > arr[largest]:
                        largest = right
