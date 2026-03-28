"""
chaos_sort.satire.bureaucracy_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Bureaucracy Sort - Requires paperwork and approval for 
every single operation.
"""

import time
from typing import List, Dict, Generator, Tuple, Any

def bureaucracy_sort(
    data: List[int],
    delay: float = 0.5,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Bureaucracy Sort - Slowed down by red tape.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': '3-5 business days',
        'current_operation': 'Submitting Form 12-B for index inspection...',
        'approvals_pending': len(data)**2
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    
    yield arr.copy(), stats.copy()
    
    # Basic bubble sort but with heavy red tape
    for i in range(n):
        for j in range(0, n - i - 1):
            stats['approvals_pending'] -= 1
            stats['comparisons'] += 1
            stats['current_operation'] = f'Requesting permit to compare [{j}] and [{j+1}]...'
            stats['time_elapsed'] = time.time() - start_time
            yield arr.copy(), stats.copy()
            if delay > 0: time.sleep(delay * 0.5)
            
            if arr[j] > arr[j+1]:
                stats['current_operation'] = f'Approval received. Stamping Form 45-X for swap...'
                yield arr.copy(), stats.copy()
                if delay > 0: time.sleep(delay)
                
                arr[j], arr[j+1] = arr[j+1], arr[j]
                stats['swaps'] += 1
                stats['current_operation'] = f'Swap executed. Notifying the regional supervisor.'
                yield arr.copy(), stats.copy()
                if delay > 0: time.sleep(delay * 0.5)
                
    stats['current_operation'] = '[DONE] Sorting finalized by the Department of Order.'
    yield arr, stats
