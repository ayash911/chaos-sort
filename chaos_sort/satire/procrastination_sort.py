"""
chaos_sort.satire.procrastination_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Procrastination Sort - Waits until the last possible 
moment to do anything.
"""

import time
import random
from typing import List, Dict, Generator, Tuple, Any

def procrastination_sort(
    data: List[int],
    delay: float = 0.5,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Procrastination Sort - Wait, wait, wait... then maybe sort one pair.
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'Eventually (TM)',
        'current_operation': 'Checking emails first...',
        'caffeine_level': 20
    }
    
    start_time = time.time()
    arr = data.copy()
    
    yield arr.copy(), stats.copy()
    
    distractions = [
        "Thinking about lunch...",
        "Scrolling through StackOverflow...",
        "Is it Friday yet?",
        "Need more coffee.",
        "Refactoring the README for the 5th time.",
        "Testing the internet speed.",
        "Organizing the desktop icons."
    ]
    
    # Procrastinate for several steps
    for _ in range(3):
        stats['current_operation'] = random.choice(distractions)
        stats['caffeine_level'] += random.randint(5, 15)
        stats['time_elapsed'] = time.time() - start_time
        yield arr.copy(), stats.copy()
        if delay > 0: time.sleep(delay)
        
    # Finally, do a tiny bit of work
    stats['current_operation'] = 'Fine, I will do ONE swap.'
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            stats['swaps'] += 1
            break
            
    stats['current_operation'] = '[DONE] That is enough for now. I will finish the rest tomorrow.'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
