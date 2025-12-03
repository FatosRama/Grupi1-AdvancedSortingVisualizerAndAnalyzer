def bubble_sort(vis):
    n = len(vis.arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            vis.compare(j, j + 1)
            yield
            if vis.arr[j] > vis.arr[j + 1]:
                vis.swap(j, j + 1)
                yield
                swapped = True
        if not swapped:
            break
    vis.mark_sorted()