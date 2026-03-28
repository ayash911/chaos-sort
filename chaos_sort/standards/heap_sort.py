"""
chaos_sort.standards.heap_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Heap Sort using generator-based execution for visualization.

Time Complexity: O(n log n)
Space Complexity: O(1)
Stable: No
"""

import time
from typing import List, Dict, Generator, Tuple, Any


def heap_sort(
    data: List[int],
    delay: float = 0.0,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Heap Sort - Comparison-based sorting algorithm based on a Binary Heap data structure.
    
    Parameters
    ----------
    data : List[int]
        The array to sort
    delay : float, optional
        Artificial delay between operations for visualization (default: 0.0)
    **kwargs
        Additional parameters
        
    Yields
    ------
    Tuple[List[int], Dict[str, Any]]
        Current state of the array and statistics dictionary
    """
    
    # Initialize statistics
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'O(n log n)',
        'current_operation': 'Starting Heap Sort'
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    
    # Yield initial state
    yield arr.copy(), stats.copy()
    
    def heapify(n: int, i: int) -> Generator:
        """To heapify a subtree rooted with node i which is an index in arr[]."""
        nonlocal stats
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
        
        # See if left child of root exists and is greater than root
        if l < n:
            stats['comparisons'] += 1
            stats['current_operation'] = f'Heapify: comparing root [{i}] and left child [{l}]'
            yield arr.copy(), stats.copy()
            if arr[i] < arr[l]:
                largest = l
                
        # See if right child of root exists and is greater than root
        if r < n:
            stats['comparisons'] += 1
            stats['current_operation'] = f'Heapify: comparing current largest [{largest}] and right child [{r}]'
            yield arr.copy(), stats.copy()
            if arr[largest] < arr[r]:
                largest = r
                
        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] 
            stats['swaps'] += 1
            stats['current_operation'] = f'Heapify: swapping root [{i}] and largest child [{largest}]'
            stats['time_elapsed'] = time.time() - start_time
            yield arr.copy(), stats.copy()
            
            if delay > 0:
                time.sleep(delay * 0.5)
            
            # Heapify the root.
            yield from heapify(n, largest)
            
    # Build a maxheap
    stats['current_operation'] = 'Building Max Heap'
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(n, i)
        
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        stats['swaps'] += 1
        stats['current_operation'] = f'Extracting max element to [{i}]'
        stats['time_elapsed'] = time.time() - start_time
        yield arr.copy(), stats.copy()
        
        if delay > 0:
            time.sleep(delay)
            
        yield from heapify(i, 0)
        
    # Final state
    stats['current_operation'] = 'Complete'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
