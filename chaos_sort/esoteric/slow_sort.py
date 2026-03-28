"""
chaos_sort.esoteric.slow_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Slow Sort - A multiply-and-surrender algorithm with 
astronomical complexity. 
"""

import time
from typing import List, Dict, Generator, Tuple, Any

def slow_sort(
    data: List[int],
    delay: float = 0.0,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Slow Sort - A recursive algorithm that is intentionally slow.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'O(n^(log n))',
        'current_operation': 'Beginning the slow journey...'
    }
    
    start_time = time.time()
    arr = data.copy()
    
    def slow_sort_recursive(i: int, j: int) -> Generator:
        nonlocal stats
        if i >= j:
            return
        
        m = (i + j) // 2
        yield from slow_sort_recursive(i, m)
        yield from slow_sort_recursive(m + 1, j)
        
        stats['comparisons'] += 1
        stats['current_operation'] = f'Comparing extremes: [{i}] and [{j}]'
        stats['time_elapsed'] = time.time() - start_time
        yield arr.copy(), stats.copy()
        
        if arr[j] < arr[m]:
            arr[m], arr[j] = arr[j], arr[m]
            stats['swaps'] += 1
            stats['current_operation'] = f'Multiplying and surrendering: Swapping [{m}] and [{j}]'
            yield arr.copy(), stats.copy()
            if delay > 0: time.sleep(delay)
            
        yield from slow_sort_recursive(i, j - 1)

    yield arr.copy(), stats.copy()
    yield from slow_sort_recursive(0, len(arr) - 1)
    
    stats['current_operation'] = '[DONE] Finally...'
    yield arr, stats
