def tree_sort(arr):
    """
    Tree Sort Algorithm using Binary Search Tree (BST).
    Returns: (sorted_list, comparisons, operations)
    """
    comparisons = 0
    operations = 0

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    root = None

    # Insertion into BST
    for num in arr:
        if root is None:
            root = Node(num)
        else:
            current = root
            while True:
                comparisons += 1
                if num < current.value:
                    if current.left is None:
                        current.left = Node(num)
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = Node(num)
                        break
                    current = current.right
        operations += 1

    # In-order traversal
    sorted_list = []
    def inorder(node):
        nonlocal operations
        if node:
            inorder(node.left)
            sorted_list.append(node.value)
            operations += 1
            inorder(node.right)

    inorder(root)

    return sorted_list, comparisons, operations