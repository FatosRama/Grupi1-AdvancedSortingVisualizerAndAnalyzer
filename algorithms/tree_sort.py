class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Tree Sort Algorithm:
# Build a Binary Search Tree (BST) from the array, then perform an
# inorder traversal to retrieve the values in sorted order.
# The visualizer (vis) updates each step for animations.

def tree_sort(vis):
        arr = vis.arr
        if not arr:
            vis.mark_sorted()
            yield
            return

        root= None
        for i, num in enumerate(arr):
            #EXPERIMENTAL DEBUG: print each insertion
            print(f"Debug: inserting {num} into BST")
            
            root=insert(root,num)
            vis.steps+=1
            if hasattr(vis,'update_display'):
                vis.update_display([i],f"Inserting {num} into BST")
            yield

        stack = []
        current = root
        idx = 0

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            arr[idx] = current.val
            yield

            idx += 1
            current = current.right

        vis.mark_sorted()
        yield

def insert(root,val):
        if not root:
            return TreeNode(val)

        if val<root.val:
            root.left=insert(root.left, val)
        else:
            root.right=insert(root.right, val)

        return root
