def counting_sort(vis):
    arr=vis.arr

    if not arr:
        vis.mark_sorted()
        yield
        return

    max_val=max(arr)
    min_val=min(arr)
    range_val=max_val-min_val+1

    count=[0]*range_val
    output=[0]*len(arr)

    for idx, num in enumerate(arr):
        count[num-min_val]+=1
        vis.steps +=1

        if hasattr(vis, "update_display"):
            vis.update_display([idx], f"Counting: {num}")

        yield