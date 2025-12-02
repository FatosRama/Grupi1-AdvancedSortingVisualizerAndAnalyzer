def heap_sort(arr):
    """
    Heap Sort Algorithm.
    Params:
        arr (list[int]): Input list of integers.
    Returns:
        tuple: (sorted_list, comparisons, swaps)
    """
    if not arr:
        return [],0,0

    arr=arr.copy()
    n=len(arr)

    comparisons=0
    swaps=0

    def heapify(n,i):
        nonlocal comparisons,swaps
        largest=i
        left=2*i+1
        right=2*i+2

        if left<n:
            comparisons +=1
            if arr[left]>arr[largest]:
                largest=left

        if right<n:
            comparisons+=1
            if arr[right]>arr[largest]:
                largest=right

        if largest!=i:
            arr[i],arr[largest]=arr[largest],arr[i]
            swaps+=1
            heapify(n,largest)

    for i in range(n // 2-1, -1, -1):
        heapify(n,i)

    for i in range(n-1, 0 ,-1):
        arr[0], arr[i]=arr[i], arr[0]
        swaps+=1
        heapify(i,0)

    return arr,comparisons,swaps