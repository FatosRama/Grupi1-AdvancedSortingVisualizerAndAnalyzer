def radix_sort(arr):
    """
    Radix Sort Algorithm (base 10).
    Params:
        arr (list[int]): Input list of integers.
    Returns:
        tuple: (sorted_list, operations count)
    Note:
        Radix Sort is stable and non-compartive.
        Track operations, not comparisons.
    """
    if not arr:
        return [],0

    arr= arr.copy()
    operations= 0

    negatives=[x for x in arr if x<0]
    non_negatives=[x for x in arr if x>=0]

    def counting_sort_by_digit(array, exp):
        nonlocal operations
        output= [0] * len(array)
        count= [0] *10

        for num in array:
            digit=(num // exp)%10
            count[digit] +=1
            operations +=1

        for i in range(1,10):
            count[i]+=count[i-1]
            operations +=1

        for num in reversed(array):
            digit=(num // exp)%10
            count[digit]-=1
            output[count[digit]]=num
            operations+=1

        return output

    if non_negatives:
        max_val=max(non_negatives)
        exp=1
        while max_val // exp>0:
            non_negatives=counting_sort_by_digit(non_negatives,exp)
            exp*=10
            operations+=1

    if negatives:
        negatives=[-x for x in negatives]
        max_val=max(negatives)
        exp=1
        while max_val // exp>0:
            negatives= counting_sort_by_digit(negatives,exp)
            exp*=10
            operations+=1
        negatives=[-x for x in reversed(negatives)]

    sorted_arr=negatives+non_negatives
    return sorted_arr, operations