def selection_sort(vis):
    arr = vis.arr
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            vis.compare(j, min_idx)
            yield
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            vis.swap(i, min_idx)
            yield

    vis.mark_sorted()
    yield