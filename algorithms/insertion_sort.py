def insertion_sort(vis):
    arr = vis.arr
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0:
            vis.compare(j, i)
            yield
            if arr[j] > key:
                vis.swap(j, j + 1)
                yield
                j -= 1
            else:
                break

    vis.mark_sorted()
    yield