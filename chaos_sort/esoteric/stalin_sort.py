"""
chaos_sort.esoteric.stalin_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Stalin Sort - A simple, single-pass destructive sort.
Elements that are not in increasing order are "sent to the gulag" (deleted).

Complexity: O(n)
Stability: Yes (survivors maintain relative order)
"""

import time
from typing import List, Dict, Generator, Tuple, Any

def stalin_sort(
    data: List[int],
    delay: float = 0.05,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Stalin Sort - Deletes any element that is not in increasing order.
    
    "I believe in one thing only, the power of human will." - Joseph Stalin
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'O(n)',
        'current_operation': 'Comrade, we are starting the purge...',
        'elements_purged': 0,
        'original_size': len(data)
    }
    
    start_time = time.time()
    arr = data.copy()
    
    yield arr.copy(), stats.copy()
    
    if not arr:
        yield arr, stats
        return

    i = 0
    while i < len(arr) - 1:
        stats['comparisons'] += 1
        stats['time_elapsed'] = time.time() - start_time
        
        # Check if next element is in order
        if arr[i] > arr[i+1]:
            # Purge the offending element
            purged_val = arr.pop(i+1)
            stats['elements_purged'] += 1
            stats['current_operation'] = f'Purging element {purged_val} for lack of order.'
            yield arr.copy(), stats.copy()
            if delay > 0: time.sleep(delay)
        else:
            # Move to next element
            i += 1
            stats['current_operation'] = f'Element {arr[i]} is loyal to the party.'
            yield arr.copy(), stats.copy()
    
    stats['current_operation'] = f'[DONE] The array is now unified. Survivors: {len(arr)}'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
