"""
chaos_sort.standards.radix_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Radix Sort using generator-based execution for visualization.

Time Complexity: O(nk)
Space Complexity: O(n+k)
Stable: Yes
"""

import time
from typing import List, Dict, Generator, Tuple, Any


def radix_sort(
    data: List[int],
    delay: float = 0.0,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Radix Sort - Non-comparative sorting algorithm. It avoids comparison 
    by creating and distributing elements into buckets according to their radix.
    
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
        'theoretical_time': 'O(nk)',
        'current_operation': 'Starting Radix Sort'
    }
    
    start_time = time.time()
    arr = data.copy()
    
    if not arr:
        yield arr, stats
        return

    # Find the maximum number to know number of digits
    max_val = max(arr)
    exp = 1 # 1, 10, 100, ...
    
    # Yield initial state
    yield arr.copy(), stats.copy()
    
    while max_val // exp > 0:
        stats['current_operation'] = f'Sorting digits at place value: {exp}'
        
        # Counting sort for this digit
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        
        # Store count of occurrences in count[]
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
            stats['current_operation'] = f'Counting: arr[{i}] has digit {(arr[i]//exp)%10}'
            stats['swaps'] += 1 # Counting as an operation
            yield arr.copy(), stats.copy()
            if delay > 0: time.sleep(delay * 0.1)
            
        # Change count[i] so that count[i] now contains actual
        # position of this digit in output[]
        for i in range(1, 10):
            count[i] += count[i - 1]
            
        # Build the output array
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1
            
        # Copy the output array to arr[], so that arr[] now
        # contains sorted numbers according to current digit
        for i in range(n):
            arr[i] = output[i]
            stats['swaps'] += 1
            stats['current_operation'] = f'Updating arr[{i}] with value {arr[i]}'
            stats['time_elapsed'] = time.time() - start_time
            yield arr.copy(), stats.copy()
            if delay > 0:
                time.sleep(delay)
                
        exp *= 10
        
    # Final state
    stats['current_operation'] = 'Complete'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
