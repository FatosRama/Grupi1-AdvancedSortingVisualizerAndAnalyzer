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