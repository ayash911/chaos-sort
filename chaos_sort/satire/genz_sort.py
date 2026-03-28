"""
chaos_sort.satire.genz_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Gen Z Sort - Deletes elements with "bad vibes" (values it 
randomly decides it doesn't like).
"""

import time
import random
from typing import List, Dict, Generator, Tuple, Any

def genz_sort(
    data: List[int],
    delay: float = 0.2,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Gen Z Sort - Sorting by vibe check.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'Depends on the aesthetic',
        'current_operation': 'Performing vibe check on the array...',
        'canceled_elements': 0
    }
    
    start_time = time.time()
    arr = data.copy()
    
    yield arr.copy(), stats.copy()
    
    # 1. Decide what is "bad vibes" today
    bad_vibe_threshold = random.randint(min(arr) if arr else 0, max(arr) if arr else 100)
    stats['current_operation'] = f'Manifesting better vibes (Threshold: {bad_vibe_threshold}).'
    yield arr.copy(), stats.copy()
    if delay > 0: time.sleep(delay)

    # 2. Cancel elements with bad vibes
    i = 0
    while i < len(arr):
        stats['time_elapsed'] = time.time() - start_time
        if arr[i] > bad_vibe_threshold:
            stats['current_operation'] = f'Element {arr[i]} has problematic vibes. Canceled.'
            val = arr.pop(i)
            stats['canceled_elements'] += 1
            yield arr.copy(), stats.copy()
            if delay > 0: time.sleep(delay)
        else:
            stats['current_operation'] = f'{arr[i]} is highly aesthetic. No cap.'
            yield arr.copy(), stats.copy()
            i += 1
            
    stats['current_operation'] = '[DONE] Array is now valid and sorted. Slay.'
    yield arr, stats
