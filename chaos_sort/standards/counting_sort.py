"""
chaos_sort.standards.counting_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Counting Sort using generator-based execution for visualization.

Time Complexity: O(n+k)
Space Complexity: O(k)
Stable: Yes
"""

import time
from typing import List, Dict, Generator, Tuple, Any


def counting_sort(
    data: List[int],
    delay: float = 0.0,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Counting Sort - Sorts the elements of an array by counting the number 
    of occurrences of each unique element in the array.
    
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
        'theoretical_time': 'O(n+k)',
        'current_operation': 'Starting Counting Sort'
    }
    
    start_time = time.time()
    arr = data.copy()
    
    if not arr:
        yield arr, stats
        return

    # Yield initial state
    yield arr.copy(), stats.copy()
    
    # 1. Find max element to define range
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    stats['current_operation'] = f'Range: [{min_val}, {max_val}], defined by {range_val} values'
    yield arr.copy(), stats.copy()
    
    # 2. Initialize count array
    count = [0] * range_val
    output = [0] * len(arr)
    
    # 3. Store count of each element
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
        stats['swaps'] += 1 # Counting as modification
        stats['current_operation'] = f'Counting occurrences: {arr[i]}'
        stats['time_elapsed'] = time.time() - start_time
        yield arr.copy(), stats.copy()
        if delay > 0:
            time.sleep(delay * 0.2)
            
    # 4. Update count array for positions
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    # 5. Build output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
        
    # 6. Copy output back to arr
    for i in range(len(arr)):
        arr[i] = output[i]
        stats['swaps'] += 1
        stats['current_operation'] = f'Reconstructing array: arr[{i}] = {arr[i]}'
        stats['time_elapsed'] = time.time() - start_time
        yield arr.copy(), stats.copy()
        if delay > 0:
            time.sleep(delay)
            
    # Final state
    stats['current_operation'] = 'Complete'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
