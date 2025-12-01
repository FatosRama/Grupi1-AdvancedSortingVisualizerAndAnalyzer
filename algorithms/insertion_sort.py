def insertion_sort(arr):
    """
    Insertion Sort Algorithm.
    Params:
        arr (list[int]): Input list of integers
    Returns:
        tuple: (sorted_list, comparisons, operations)
    Note:
        Track comparisons and operations (shifts + placements) for visualization and analysis.
    """
    comparisons = 0
    operations = 0
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                operations += 1
                j -= 1
            else:
                break

        arr[j + 1] = key
        operations += 1

    return arr, comparisons, operations


def insertion_sort_with_steps(arr):
    """
    Insertion Sort with step-by-step recording for real-time animation/visualization.
    Returns: (sorted_array, steps, comparisons, operations)
    """
    arr = arr.copy()
    steps = []
    comparisons = 0
    operations = 0

    # Initial state
    steps.append({
        'array': arr.copy(),
        'action': 'start',
        'description': 'Starting Insertion Sort'
    })

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Select the element to insert
        steps.append({
            'array': arr.copy(),
            'action': 'select',
            'i': i,
            'description': f'Select element {key} (index {i})'
        })

        while j >= 0:
            comparisons += 1
            steps.append({
                'array': arr.copy(),
                'action': 'compare',
                'i': i,
                'j': j,
                'description': f'Compare {arr[j]} and {key}'
            })

            if arr[j] > key:
                arr[j + 1] = arr[j]
                operations += 1
                steps.append({
                    'array': arr.copy(),
                    'action': 'shift',
                    'j': j,
                    'description': f'Shift {arr[j]} one position right'
                })
                j -= 1
            else:
                steps.append({
                    'array': arr.copy(),
                    'action': 'stop',
                    'j': j,
                    'description': f'{arr[j]} ≤ {key} → stop shifting'
                })
                break

        arr[j + 1] = key
        operations += 1
        steps.append({
            'array': arr.copy(),
            'action': 'insert',
            'pos': j + 1,
            'description': f'Insert {key} at position {j + 1}'
        })

    # Final state
    steps.append({
        'array': arr.copy(),
        'action': 'finished',
        'description': 'Array fully sorted!'
    })

    return arr, steps, comparisons, operations