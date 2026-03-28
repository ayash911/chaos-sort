"""
chaos_sort.esoteric.stooge_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Stooge Sort - A recursive sort that is famously 
inefficient but mathematically sound.
"""

import time
from typing import List, Dict, Generator, Tuple, Any

def stooge_sort(
    data: List[int],
    delay: float = 0.05,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Stooge Sort - Sorts first 2/3, last 2/3, then first 2/3 again.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'O(n^2.7)',
        'current_operation': 'Assembling the Stooges...'
    }
    
    start_time = time.time()
    arr = data.copy()
    
    def stooge_sort_recursive(l: int, h: int) -> Generator:
        nonlocal stats
        if l >= h:
            return
        
        stats['comparisons'] += 1
        stats['current_operation'] = f'Comparing: [{l}] and [{h}]'
        stats['time_elapsed'] = time.time() - start_time
        yield arr.copy(), stats.copy()
        
        if arr[l] > arr[h]:
            arr[l], arr[h] = arr[h], arr[l]
            stats['swaps'] += 1
            stats['current_operation'] = f'Swapping: [{l}] and [{h}]'
            yield arr.copy(), stats.copy()
            if delay > 0: time.sleep(delay)
            
        if h - l + 1 > 2:
            t = (h - l + 1) // 3
            # Sort first 2/3
            yield from stooge_sort_recursive(l, h - t)
            # Sort last 2/3
            yield from stooge_sort_recursive(l + t, h)
            # Sort first 2/3 again
            yield from stooge_sort_recursive(l, h - t)

    yield arr.copy(), stats.copy()
    yield from stooge_sort_recursive(0, len(arr) - 1)
    
    stats['current_operation'] = '[DONE] Stooge Sort complete.'
    yield arr, stats
