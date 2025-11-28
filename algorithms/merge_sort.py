def merge_sort(arr):
    """
    Merge Sort Algorithm.
    Params:
        arr (list[int]): Input list of integers
    Returns:
        tuple: (sorted_list, comparisons, operations)
    Note:
        Track comparisons and operations (element placements) for analysis.
    """
    comparisons = 0
    operations = 0

    def merge(left, right):
        nonlocal comparisons, operations
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            comparisons += 1

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

            operations += 1

        while i < len(left):
            result.append(left[i])
            i += 1
            operations += 1

        while j < len(right):
            result.append(right[j])
            j += 1
            operations += 1

        return result

    def divide(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = divide(arr[:mid])
        right = divide(arr[mid:])
        return merge(left, right)

    sorted_list = divide(arr.copy())
    return sorted_list, comparisons, operations
