"""
chaos_sort.standards.selection_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Selection Sort using generator-based execution for visualization.

Time Complexity: O(n²)
Space Complexity: O(1)
Stable: No
"""

import time
from typing import List, Dict, Generator, Tuple, Any


def selection_sort(
    data: List[int],
    delay: float = 0.0,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Selection Sort - Sorts an array by repeatedly finding the minimum
    element from unsorted part and putting it at the beginning.
    
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
        'theoretical_time': 'O(n^2)',
        'current_operation': 'Starting Selection Sort'
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    
    # Yield initial state
    yield arr.copy(), stats.copy()
    
    for i in range(n):
        min_idx = i
        stats['current_operation'] = f'New pass: current minimum at [{min_idx}]'
        yield arr.copy(), stats.copy()
        
        for j in range(i + 1, n):
            stats['comparisons'] += 1
            stats['current_operation'] = f'Comparing: [{j}] with min at [{min_idx}]'
            stats['time_elapsed'] = time.time() - start_time
            yield arr.copy(), stats.copy()
            
            if delay > 0:
                time.sleep(delay)
            
            if arr[j] < arr[min_idx]:
                min_idx = j
                stats['current_operation'] = f'Found new minimum at [{min_idx}]'
                yield arr.copy(), stats.copy()
        
        # Swap the found minimum element with the first element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            stats['swaps'] += 1
            stats['current_operation'] = f'Swapping: [{i}] and [{min_idx}]'
            
            stats['time_elapsed'] = time.time() - start_time
            yield arr.copy(), stats.copy()
            
            if delay > 0:
                time.sleep(delay)
            
    # Final state
    stats['current_operation'] = 'Complete'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
