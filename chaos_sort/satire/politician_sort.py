"""
chaos_sort.satire.politician_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Politician Sort - Declares the array sorted and blames the 
previous state/predecessor for any discrepancies.
"""

import time
from typing import List, Dict, Generator, Tuple, Any

def politician_sort(
    data: List[int],
    delay: float = 0.2,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Politician Sort - Never actually sorts, just claims success.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'Immediate (by decree)',
        'current_operation': 'Launching campaign for a sorted future...',
        'approval_rating': 45.5,
        'broken_promises': 0
    }
    
    start_time = time.time()
    arr = data.copy()
    
    yield arr.copy(), stats.copy()
    
    # 1. Inspect the array and point out "problems" inherited from the previous dev
    stats['current_operation'] = 'Inherited a mess from the previous administration.'
    stats['comparisons'] += len(arr)
    yield arr.copy(), stats.copy()
    if delay > 0: time.sleep(delay)

    # 2. Make a big announcement
    stats['current_operation'] = 'I have a plan to sort this array like never before.'
    yield arr.copy(), stats.copy()
    if delay > 0: time.sleep(delay)

    # 3. Blame everyone else
    if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        stats['current_operation'] = 'Disorder is a choice made by the previous developers.'
        stats['broken_promises'] += 1
        yield arr.copy(), stats.copy()
        if delay > 0: time.sleep(delay)

    # 4. Declare victory without doing anything
    stats['current_operation'] = '[DECLARATION]: This array is now "Effectively Sorted".'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
