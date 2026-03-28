"""
chaos_sort.standards.bubble_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Bubble Sort using generator-based execution for visualization.

Time Complexity: O(n²)
Space Complexity: O(1)
Stable: Yes
"""

import time
from typing import List, Dict, Generator, Tuple, Any


def bubble_sort(
    data: List[int],
    delay: float = 0.0,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Bubble Sort - Simplest sorting algorithm that works by repeatedly
    swapping the adjacent elements if they are in wrong order.
    
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
        'current_operation': 'Starting Bubble Sort'
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    
    # Yield initial state
    yield arr.copy(), stats.copy()
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            stats['comparisons'] += 1
            stats['current_operation'] = f'Comparing: [{j}] and [{j+1}]'
            stats['time_elapsed'] = time.time() - start_time
            yield arr.copy(), stats.copy()
            
            if delay > 0:
                time.sleep(delay)
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                stats['swaps'] += 1
                stats['current_operation'] = f'Swapping: [{j}] and [{j+1}]'
                swapped = True
                
                stats['time_elapsed'] = time.time() - start_time
                yield arr.copy(), stats.copy()
                
                if delay > 0:
                    time.sleep(delay)
        
        if not swapped:
            # Optimization: if no two elements were swapped by inner loop, then break
            stats['current_operation'] = 'Optimized early exit: Array is sorted'
            break
            
    # Final state
    stats['current_operation'] = 'Complete'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
