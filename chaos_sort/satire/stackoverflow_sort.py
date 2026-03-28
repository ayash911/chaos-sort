"""
chaos_sort.satire.stackoverflow_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of StackOverflow Sort - Simulated "web scraping" and "copy-pasting" 
from the community.
"""

import time
import random
from typing import List, Dict, Generator, Tuple, Any

def stackoverflow_sort(
    data: List[int],
    delay: float = 0.3,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    StackOverflow Sort - Searching for a solution someone else already wrote.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'Depends on your internet speed',
        'current_operation': 'Searching: "how sort array python fast"...',
        'tabs_open': 12
    }
    
    start_time = time.time()
    arr = data.copy()
    
    yield arr.copy(), stats.copy()
    
    searches = [
        "python sort list fastest way",
        "why is my bubble sort O(n^3)",
        "copy paste quicksort python",
        "marked as duplicate by Jon Skeet"
    ]
    
    for query in searches:
        stats['current_operation'] = f'Google Search: "{query}"'
        stats['tabs_open'] += random.randint(1, 4)
        stats['time_elapsed'] = time.time() - start_time
        yield arr.copy(), stats.copy()
        if delay > 0: time.sleep(delay)
        
    stats['current_operation'] = 'Found a snippet! Copy-pasting from Top Answer...'
    arr.sort() # Copy-pasting the "built-in" solution
    import math
    stats['comparisons'] = int(len(arr) * math.log2(len(arr))) if len(arr) > 1 else 0
    stats['swaps'] = len(arr) // 2
    yield arr.copy(), stats.copy()
    if delay > 0: time.sleep(delay)
    
    stats['current_operation'] = '[DONE] Upvoted the answer. Closing 42 tabs.'
    yield arr, stats
