"""
chaos_sort.satire.gaslight_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Gaslight Sort - Changes the original data to make 
it appear sorted without actually sorting.
"""

import time
import random
from typing import List, Dict, Generator, Tuple, Any

def gaslight_sort(
    data: List[int],
    delay: float = 0.3,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Gaslight Sort - Alters reality to fit the narrative.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'Depends on how much you trust me',
        'current_operation': 'Adjusting values to reflect the truth...',
        'reality_distortion': 100
    }
    
    start_time = time.time()
    arr = data.copy()
    
    yield arr.copy(), stats.copy()
    
    # 1. Distort reality: literally change values to be sorted
    stats['current_operation'] = 'The elements were always like this. You just misremembered.'
    
    # Sort the array internally but pretend we didn't
    arr.sort()
    import math
    stats['comparisons'] = int(len(arr) * math.log2(len(arr))) if len(arr) > 1 else 0
    
    for i in range(len(arr)):
        stats['current_operation'] = f'Adjusting index {i} back to what it "should" be.'
        stats['time_elapsed'] = time.time() - start_time
        yield arr.copy(), stats.copy()
        if delay > 0: time.sleep(delay)
        
    stats['current_operation'] = '[DONE] See? It was sorted all along. Stop questioning me.'
    yield arr, stats
