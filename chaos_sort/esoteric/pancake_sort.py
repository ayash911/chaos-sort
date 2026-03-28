"""
chaos_sort.esoteric.pancake_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Pancake Sort - Sorts by reversing prefixes.
"""

import time
from typing import List, Dict, Generator, Tuple, Any

def pancake_sort(
    data: List[int],
    delay: float = 0.02,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Pancake Sort - Repeatedly flips pancakes to put the largest one on top and then at the bottom.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'O(n^2)',
        'current_operation': 'Heating up the griddle...'
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    
    yield arr.copy(), stats.copy()
    
    def flip(k: int):
        nonlocal stats
        stats['swaps'] += 1
        stats['current_operation'] = f'Flipping prefix [0:{k}]'
        left, right = 0, k
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
    for curr_size in range(n, 1, -1):
        # Find index of maximum element in arr[0..curr_size-1]
        max_idx = 0
        for i in range(1, curr_size):
            stats['comparisons'] += 1
            if arr[i] > arr[max_idx]:
                max_idx = i
        
        if max_idx != curr_size - 1:
            # Move max to the top
            if max_idx != 0:
                flip(max_idx)
                yield arr.copy(), stats.copy()
                if delay > 0: time.sleep(delay)
            
            # Move max to the end
            flip(curr_size - 1)
            yield arr.copy(), stats.copy()
            if delay > 0: time.sleep(delay)
            
    stats['current_operation'] = '[DONE] Pancakes stacked and sorted.'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
