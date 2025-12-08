def merge_sort(vis, left=0, right=None):
    if right is None:
        right = len(vis.arr) - 1

    if left < right:
        mid = (left + right) // 2

        yield from merge_sort(vis, left, mid)
        yield from merge_sort(vis, mid + 1, right)

        yield from merge(vis, left, mid, right)

    if left == 0 and right == len(vis.arr) - 1:
        vis.mark_sorted()
        yield


def merge(vis, left, mid, right):
    arr = vis.arr
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        vis.compare(left + i, mid + 1 + j)
        yield

        if left_part[i] <= right_part[j]:
            if arr[k] != left_part[i]:
                arr[k] = left_part[i]
                # Visualize the copy
                vis.steps += 1
                if hasattr(vis, 'update_display'):
                    vis.update_display([k], "Merging")
                yield
            i += 1
        else:
            if arr[k] != right_part[j]:
                arr[k] = right_part[j]
                vis.steps += 1
                if hasattr(vis, 'update_display'):
                    vis.update_display([k], "Merging")
                yield
            j += 1
        k += 1

    while i < len(left_part):
        if arr[k] != left_part[i]:
            arr[k] = left_part[i]
            vis.steps += 1
            if hasattr(vis, 'update_display'):
                vis.update_display([k], "Merging")
            yield
        i += 1
        k += 1

    while j < len(right_part):
        if arr[k] != right_part[j]:
            arr[k] = right_part[j]
            vis.steps += 1
            if hasattr(vis, 'update_display'):
                vis.update_display([k], "Merging")
            yield
        j += 1
        k += 1