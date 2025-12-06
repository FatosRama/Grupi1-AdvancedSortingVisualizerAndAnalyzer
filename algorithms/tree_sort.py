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

def insert(root,val):
        if not root:
            return TreeNode(val)

        if val<root.val:
            root.left=insert(root.left, val)
        else:
            root.right=insert(root.right, val)