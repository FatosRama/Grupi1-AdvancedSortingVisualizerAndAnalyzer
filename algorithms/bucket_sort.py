def bucket_sort(arr):
    if not arr:
        yield arr[:], 0, 0, ()
        return

    arr = arr.copy()
    n = len(arr)
    comparisons = writes = 0

    min_val, max_val = min(arr), max(arr)
    if max_val == min_val:
        yield arr[:], comparisons, writes, ()
        return

    buckets = [[] for _ in range(n)]

    for i, num in enumerate(arr):
        bucket_idx = int((num - min_val) / (max_val - min_val) * (n - 1))
        buckets[bucket_idx].append((i, num))
        yield arr[:], comparisons, writes, (i,)

    pos = 0
    for bucket in buckets:
        for i in range(1, len(bucket)):
            key_idx, key = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j][1] > key:
                comparisons += 1
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = (key_idx, key)
        for orig_idx, value in bucket:
            arr[pos] = value
            writes += 1
            yield arr[:], comparisons, writes, (pos,)
            pos += 1

    yield arr[:], comparisons, writes, ()