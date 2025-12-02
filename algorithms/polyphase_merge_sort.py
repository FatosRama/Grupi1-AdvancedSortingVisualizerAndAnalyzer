def polyphase_merge_sort(arr):
    arr = arr.copy()
    n = len(arr)
    comparisons = writes = 0

    if n <= 1:
        yield arr[:], comparisons, writes, ()
        return

    from collections import deque

    tapes = [deque(), deque(), deque()]
    
    fib = [0, 1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    
    idx = 0
    for size in fib[-2:0:-1]:  
        for _ in range(min(size, n - idx)):
            if idx < n:
                tapes[0].append(arr[idx])
                arr[idx] = tapes[0][-1] 
                yield arr[:], comparisons, writes, (idx,)
                idx += 1

    while any(tapes[1]) or any(tapes[2]):
        source = None
        for t in range(1, 3):
            if tapes[t]:
                source = t
                break

        if source is None:
            break

        while tapes[source]:
            val = tapes[source].popleft()
            tapes[0].append(val)
            
            pos = len(tapes[0]) - 1
            if pos < n:
                arr[pos] = val
                writes += 1
                yield arr[:], comparisons, writes, (pos,)

        tapes.append(tapes.popleft())

    for i, val in enumerate(tapes[0]):
        if i < n:
            arr[i] = val
            writes += 1
            yield arr[:], comparisons, writes, (i,)

    yield arr[:], comparisons, writes, ()