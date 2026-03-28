"""
chaos_sort.satire.intimidation_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Intimidation Sort - Claims the array is sorted and 
pressures the user into agreeing.
"""

import time
from typing import List, Dict, Generator, Tuple, Any

def intimidation_sort(
    data: List[int],
    delay: float = 0.4,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Intimidation Sort - Gaslights the user into thinking order exists.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'Immediate',
        'current_operation': 'Checking your credentials...',
        'pressure_level': 100
    }
    
    start_time = time.time()
    arr = data.copy()
    
    yield arr.copy(), stats.copy()
    
    threats = [
        "Are you SURE this isn't sorted?",
        "Only junior devs would say this is unsorted.",
        "My senior architect says it's perfectly organized.",
        "If you don't see the order, that's your problem.",
        "I've been sorting for 20 years, I know what I see."
    ]
    
    for threat in threats:
        stats['current_operation'] = f'[INTIMIDATION]: {threat}'
        stats['time_elapsed'] = time.time() - start_time
        yield arr.copy(), stats.copy()
        if delay > 0: time.sleep(delay)
        
    stats['current_operation'] = '[DONE] Sorted. Do not ask questions.'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
