def shell_sort(arr):
    arr = arr.copy()
    n = len(arr)
    comparisons = writes = 0

    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap:
                comparisons += 1
                yield arr[:], comparisons, writes, (j - gap, j)

                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    writes += 1
                    j -= gap
                    yield arr[:], comparisons, writes, (j, j + gap)
                else:
                    break

            arr[j] = temp
            writes += 1
            yield arr[:], comparisons, writes, (j,)

        gap //= 3

    yield arr[:], comparisons, writes, ()