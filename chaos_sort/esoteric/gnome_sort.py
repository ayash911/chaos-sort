"""
chaos_sort.esoteric.gnome_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Gnome Sort - The garden gnome's sorting algorithm.
"""

import time
from typing import List, Dict, Generator, Tuple, Any

def gnome_sort(
    data: List[int],
    delay: float = 0.02,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Gnome Sort - Moving like a gnome: step forward if sorted, step back if swapped.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'O(n^2)',
        'current_operation': 'A gnome enters the garden...'
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    index = 0
    
    yield arr.copy(), stats.copy()
    
    while index < n:
        if index == 0 or arr[index] >= arr[index - 1]:
            stats['current_operation'] = f'Index {index}: Good progress, moving forward.'
            index += 1
            yield arr.copy(), stats.copy()
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            stats['swaps'] += 1
            stats['current_operation'] = f'Oops! Backstepping at index {index}.'
            index -= 1
            yield arr.copy(), stats.copy()
            if delay > 0: time.sleep(delay)
            
    stats['current_operation'] = '[DONE] The garden is sorted.'
    yield arr, stats
