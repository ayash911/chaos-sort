"""
chaos_sort.standards.insertion_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Insertion Sort using generator-based execution for visualization.

Time Complexity: O(n²)
Space Complexity: O(1)
Stable: Yes
"""

import time
from typing import List, Dict, Generator, Tuple, Any


def insertion_sort(
    data: List[int],
    delay: float = 0.0,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Insertion Sort - Builds the final sorted array one item at a time.
    It is much less efficient on large lists than more advanced algorithms.
    
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
        'current_operation': 'Starting Insertion Sort'
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    
    # Yield initial state
    yield arr.copy(), stats.copy()
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        stats['current_operation'] = f'Inserting: {key} (originally at [{i}])'
        yield arr.copy(), stats.copy()
        
        while j >= 0:
            stats['comparisons'] += 1
            stats['current_operation'] = f'Comparing: {key} with {arr[j]} at [{j}]'
            stats['time_elapsed'] = time.time() - start_time
            yield arr.copy(), stats.copy()
            
            if delay > 0:
                time.sleep(delay * 0.5)
            
            if arr[j] > key:
                arr[j + 1] = arr[j]
                stats['swaps'] += 1
                stats['current_operation'] = f'Shifting: {arr[j]} from [{j}] to [{j+1}]'
                
                stats['time_elapsed'] = time.time() - start_time
                yield arr.copy(), stats.copy()
                
                if delay > 0:
                    time.sleep(delay * 0.5)
                j -= 1
            else:
                break
        
        arr[j + 1] = key
        stats['current_operation'] = f'Placed: {key} at [{j+1}]'
        stats['time_elapsed'] = time.time() - start_time
        yield arr.copy(), stats.copy()
        
        if delay > 0:
            time.sleep(delay)
            
    # Final state
    stats['current_operation'] = 'Complete'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
