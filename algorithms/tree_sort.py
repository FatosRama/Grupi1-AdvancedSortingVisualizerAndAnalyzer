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


def tree_sort_with_steps(arr):
    """
    Tree Sort with step-by-step recording for real-time visualization.
    Returns: (sorted_array, steps, comparisons, operations)
    """
    arr = arr.copy()
    steps = []
    comparisons = 0
    operations = 0

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    root = None

    # Initial state
    steps.append({
        'array': arr.copy(),
        'action': 'start',
        'description': 'Starting Tree Sort (building BST)'
    })

    # Insertion with steps
    for idx, num in enumerate(arr):
        steps.append({
            'array': arr.copy(),
            'action': 'select',
            'index': idx,
            'value': num,
            'description': f'Insert element {num} (position {idx})'
        })

        if root is None:
            root = Node(num)
            steps.append({
                'array': arr.copy(),
                'action': 'insert_root',
                'value': num,
                'description': f'Create root node {num}'
            })
        else:
            current = root
            path = []
            while True:
                comparisons += 1
                path.append(current.value)
                steps.append({
                    'array': arr.copy(),
                    'action': 'compare',
                    'current': current.value,
                    'insert': num,
                    'description': f'Compare {num} with {current.value}'
                })

                if num < current.value:
                    if current.left is None:
                        current.left = Node(num)
                        steps.append({
                            'array': arr.copy(),
                            'action': 'insert_left',
                            'parent': current.value,
                            'value': num,
                            'description': f'Insert {num} as left child of {current.value}'
                        })
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = Node(num)
                        steps.append({
                            'array': arr.copy(),
                            'action': 'insert_right',
                            'parent': current.value,
                            'value': num,
                            'description': f'Insert {num} as right child of {current.value}'
                        })
                        break
                    current = current.right
        operations += 1

    # In-order traversal with steps
    sorted_list = []
    def inorder(node):
        nonlocal operations
        if node:
            inorder(node.left)
            sorted_list.append(node.value)
            operations += 1
            steps.append({
                'array': sorted_list.copy(),
                'action': 'visit',
                'value': node.value,
                'description': f'Visit node {node.value} (add to sorted list)'
            })
            inorder(node.right)

    inorder(root)

    # Final state
    steps.append({
        'array': sorted_list.copy(),
        'action': 'finished',
        'description': 'Tree Sort completed – array fully sorted!'
    })

    return sorted_list, steps, comparisons, operations