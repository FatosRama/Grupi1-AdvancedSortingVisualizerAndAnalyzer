def bucket_sort(vis):
    arr = vis.arr
    if not arr:
        vis.mark_sorted()
        yield
        return

# Create buckets
    n = len(arr)
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) / n if max_val != min_val else 1
    buckets = [[] for _ in range(n + 1)]

    # Put elements in buckets - VISUALIZE
    for idx, num in enumerate(arr):
        bucket_idx = int((num - min_val) / bucket_range)
        if bucket_idx >= len(buckets):
            bucket_idx = len(buckets) - 1
        buckets[bucket_idx].append(num)
        vis.steps += 1
        if hasattr(vis, 'update_display'):
            vis.update_display([idx], f"Bucket {bucket_idx}")
        yield