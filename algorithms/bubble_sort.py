def bubble_sort(arr):
    """
    Bubble Sort Algorithm.
    Params:
        arr (list[int]): Input list of integers
    Returns:
        tuple: (sorted_list, comparisons, swaps)
    """
    n=len(arr)
    comparisons= 0
    swaps= 0
    arr= arr.copy()

    for i in range(n):
        swapped= False;

        for j in range(0,n-i-1):
            comparisons+=1

            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swaps+=1
                swapped=True

        if not swapped:
            break

    return arr,comparisons,swaps
