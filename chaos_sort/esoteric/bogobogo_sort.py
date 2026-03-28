"""
chaos_sort.esoteric.bogobogo_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of BogoBogo Sort - The meta-random sort.
To sort n elements, it verifies if n-1 elements are sorted (using BogoBogo Sort)
and then shuffles until the n-th element is in place.
"""

import time
import random
from typing import List, Dict, Generator, Tuple, Any
from chaos_sort.esoteric.bogo_sort import bogo_sort

def bogobogo_sort(
    data: List[int],
    delay: float = 0.05,
    max_iterations: int = 1000,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    BogoBogo Sort - Recursively useless.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'O(inf^2)',
        'current_operation': 'Recursive randomness starting...',
        'recursion_depth': 0
    }
    
    start_time = time.time()
    arr = data.copy()
    
    def is_sorted(subset: List[int]) -> bool:
        if len(subset) <= 1: return True
        return all(subset[i] <= subset[i+1] for i in range(len(subset)-1))

    def bogobogo_recursive(n: int) -> Generator:
        nonlocal stats
        if n <= 1:
            return
        
        stats['recursion_depth'] = len(arr) - n
        
        while True:
            # Recursively sort the first n-1 elements
            yield from bogobogo_recursive(n - 1)
            
            # Check if n-th element is in place
            stats['comparisons'] += 1
            stats['current_operation'] = f'Checking if first {n} are sorted...'
            stats['time_elapsed'] = time.time() - start_time
            yield arr.copy(), stats.copy()
            
            if is_sorted(arr[:n]):
                break
            
            # Shuffle the first n elements
            sub = arr[:n]
            random.shuffle(sub)
            arr[:n] = sub
            stats['swaps'] += 1
            stats['current_operation'] = f'Shuffling first {n} elements...'
            yield arr.copy(), stats.copy()
            if delay > 0: time.sleep(delay)
            
            # Artificial break for safety
            if stats['swaps'] > max_iterations:
                stats['current_operation'] = '[TIMEOUT] Giving up on this timeline.'
                break

    yield arr.copy(), stats.copy()
    yield from bogobogo_recursive(len(arr))
    
    stats['current_operation'] = '[DONE] Statistically impossible, but complete.'
    yield arr, stats
