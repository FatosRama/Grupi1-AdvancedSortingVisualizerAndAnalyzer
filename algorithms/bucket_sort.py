def bucket_sort(vis):
    arr = vis.arr
    if not arr:
        vis.mark_sorted()
        yield
        return
