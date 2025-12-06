def quick_sort(vis):
    arr = vis.arr
    n = len(arr)
    stack = [(0, n - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                vis.compare(j, high)
                yield

                if arr[j] <= pivot:
                    i += 1
                    if i != j:
                        vis.swap(i, j)
                        yield

            if i + 1 != high:
                vis.swap(i + 1, high)
                yield

            pivot_index = i + 1