"""
chaos_sort.satire.lottery_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Lottery Sort - 1/14M chance to actually sort the array.
"""

import time
import random
from typing import List, Dict, Generator, Tuple, Any

def lottery_sort(
    data: List[int],
    delay: float = 0.3,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Lottery Sort - Investing all CPU cycles into a single random guess.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'O(1) [if extremely lucky]',
        'current_operation': 'Buying a lottery ticket for this array...',
        'jackpot_chance': '1 in 14,000,000'
    }
    
    start_time = time.time()
    arr = data.copy()
    
    yield arr.copy(), stats.copy()
    
    # 1. Picking "Winning Numbers"
    winning_numbers = sorted(arr)
    stats['current_operation'] = 'Drawing numbers... 4... 8... 15... 16... 23... 42'
    yield arr.copy(), stats.copy()
    if delay > 0: time.sleep(delay)

    # 2. Check if we won
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        stats['current_operation'] = 'JACKPOT! It was already sorted. We are rich!'
    else:
        stats['current_operation'] = 'Better luck next time. Lost another $2 of entropy.'
        # We don't sort it, just finish. 
        # But wait, usually satire sorts finish eventually. 
        # For Lottery Sort, let's just claim it's "statistically sorted".
        
    stats['current_operation'] = '[DONE] Returning to my day job.'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
