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

    for i in range(1, len(count)):
        count[i] += count[i - 1]
        vis.steps += 1

        if hasattr(vis, "update_display"):
            vis.update_display([], "Updating counts")

        yield

    for i in range(len(arr) - 1, -1, -1):
        output_idx = count[arr[i] - min_val] - 1
        output[output_idx] = arr[i]
        count[arr[i] - min_val] -= 1
        vis.steps += 1

        if hasattr(vis, "update_display"):
            vis.update_display([i], f"Placing {arr[i]} at position {output_idx}")

        yield

    for i in range(len(arr)):
        if arr[i] != output[i]:
            arr[i] = output[i]
            vis.steps += 1

            if hasattr(vis, "update_display"):
                vis.update_display([i], f"Copying {output[i]}")

            yield

    vis.mark_sorted()
    yield