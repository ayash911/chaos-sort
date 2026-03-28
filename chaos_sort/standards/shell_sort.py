"""
chaos_sort.standards.shell_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Shell Sort using generator-based execution for visualization.

Time Complexity: O(n log n) [depends on gap sequence]
Space Complexity: O(1)
Stable: No
"""

import time
from typing import List, Dict, Generator, Tuple, Any


def shell_sort(
    data: List[int],
    delay: float = 0.0,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Shell Sort - Variation of insertion sort that allows the exchange of 
    items that are far apart.
    
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
        'theoretical_time': 'O(n^1.5) avg',
        'current_operation': 'Starting Shell Sort'
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    
    # Start with a big gap, then reduce the gap
    gap = n // 2
    
    # Yield initial state
    yield arr.copy(), stats.copy()
    
    while gap > 0:
        stats['current_operation'] = f'Current gap: {gap}'
        yield arr.copy(), stats.copy()
        
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            stats['current_operation'] = f'Evaluating arr[{i}] with gap {gap}'
            yield arr.copy(), stats.copy()
            
            while j >= gap:
                stats['comparisons'] += 1
                stats['current_operation'] = f'Comparing: {temp} and {arr[j-gap]} (gap={gap})'
                stats['time_elapsed'] = time.time() - start_time
                yield arr.copy(), stats.copy()
                
                if delay > 0:
                    time.sleep(delay * 0.5)
                
                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    stats['swaps'] += 1
                    j -= gap
                    yield arr.copy(), stats.copy()
                    
                    if delay > 0:
                        time.sleep(delay * 0.5)
                else:
                    break
            
            arr[j] = temp
            stats['swaps'] += 1
            
        gap //= 2
        
    # Final state
    stats['current_operation'] = 'Complete'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
