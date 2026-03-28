"""
chaos_sort.esoteric.quantum_bogo_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Quantum Bogo Sort - (Simulated) Destroying universes where 
the array is not sorted.
"""

import time
import random
from typing import List, Dict, Generator, Tuple, Any

def quantum_bogo_sort(
    data: List[int],
    delay: float = 0.5,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Quantum Bogo Sort - Achieve O(1) by deleting all but the lucky universe.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'O(1)*',
        'current_operation': 'Splitting into infinite timelines...',
        'universes_destroyed': 0
    }
    
    start_time = time.time()
    arr = data.copy()
    
    yield arr.copy(), stats.copy()
    
    # In my "lucky" timeline, it's sorted after one shuffle
    # We simulate the destruction of other timelines
    stats['current_operation'] = 'Checking quantum state of current timeline...'
    stats['comparisons'] += len(arr) - 1
    yield arr.copy(), stats.copy()
    if delay > 0: time.sleep(delay)

    is_sorted = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    
    if not is_sorted:
        stats['current_operation'] = '[Ouch] This universe is out of order. Destroying...'
        stats['universes_destroyed'] = 99999999 # Simulated many destructions
        yield arr.copy(), stats.copy()
        if delay > 0: time.sleep(delay)
        
        # We "hop" to the sorted timeline
        arr.sort()
        stats['current_operation'] = '[JUMP] Entering the sorted timeline.'
        yield arr.copy(), stats.copy()
    else:
        stats['current_operation'] = 'Lucky! This universe was already sorted.'
        yield arr.copy(), stats.copy()

    stats['current_operation'] = '[DONE] Only the sorted universe remains.'
    yield arr, stats
