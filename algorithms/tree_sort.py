class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def tree_sort(vis):
        arr = vis.arr
        if not arr:
            vis.mark_sorted()
            yield
            return
