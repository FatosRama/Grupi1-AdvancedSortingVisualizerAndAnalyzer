def radix_sort(vis):
    arr=vis.arr
    if not arr:
        vis.mark_sorted()
        yield
        return

    max_num=max(arr)
    exp=1

    while max_num // exp>0:
        counting_sort_radix(vis,exp)
        exp *=10

    vis.mark_sorted()
    yield

def counting_sort_radix(vis, exp):
        arr = vis.arr
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
            vis.steps += 1
            if hasattr(vis, 'update_display'):
                vis.update_display([i], f"Digit {index} (exp={exp})")
            yield
            
        for i in range(1, 10):
            count[i] += count[i - 1]
            vis.steps += 1
            yield

        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output_idx = count[index] - 1
            output[output_idx] = arr[i]
            count[index] -= 1
            vis.steps += 1
            if hasattr(vis, 'update_display'):
                vis.update_display([i], f"Placing based on digit {index}")
            yield

        for i in range(n):
            if arr[i] != output[i]:
                arr[i] = output[i]
                vis.steps += 1
                if hasattr(vis, 'update_display'):
                    vis.update_display([i], f"Updating position {i}")
                yield
