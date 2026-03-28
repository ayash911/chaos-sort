"""
chaos_sort.esoteric.spaghetti_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Spaghetti Sort - A physical simulation sorting algorithm.
In reality, you hold dry spaghetti sticks and lower them onto a table. 
The tallest one hits the hand first.
"""

import time
from typing import List, Dict, Generator, Tuple, Any

def spaghetti_sort(
    data: List[int],
    delay: float = 0.1,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Spaghetti Sort - Simulated physical sorting.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'O(n)',
        'current_operation': 'Boiling the water (simulated)...'
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    
    yield arr.copy(), stats.copy()
    
    # Simulation: We find the max and "lower the hand"
    if not arr: return
    
    max_val = max(arr)
    sorted_arr = []
    original_indices = list(range(n))
    
    # We "pull" elements out as they are reached
    # To simulate, we filter and sort by value
    current_height = max_val
    
    while len(sorted_arr) < n:
        stats['current_operation'] = f'Lowering hand... Current height: {current_height}'
        stats['time_elapsed'] = time.time() - start_time
        
        # Check which "spaghetti" hit the hand
        hits = [i for i in range(len(arr)) if arr[i] == current_height]
        
        if hits:
            for hit_idx in sorted(hits, reverse=True):
                val = arr.pop(hit_idx)
                sorted_arr.insert(0, val)
                stats['current_operation'] = f'[HIT] Grabbed spaghetti of height {val}'
                yield arr.copy() + sorted_arr, stats.copy()
                if delay > 0: time.sleep(delay)
        else:
            yield arr.copy() + sorted_arr, stats.copy()
            
        current_height -= 1
        if current_height < 0: break
        
    stats['current_operation'] = '[DONE] All spaghetti collected in order.'
    yield sorted_arr, stats
