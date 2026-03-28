"""
chaos_sort.esoteric.sleep_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Sleep Sort - Sorts by sleeping for a duration equal to each 
element's value. 

Disclaimer: This is a simulation. Real sleep sort requires multithreading.
"""

import time
from typing import List, Dict, Generator, Tuple, Any

def sleep_sort(
    data: List[int],
    delay: float = 0.01,
    scale_factor: float = 0.1,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Sleep Sort - Elements "wake up" in order.
    
    Parameters
    ----------
    scale_factor : float
        Ratio of value to sleep time (default: 0.1s per unit)
    """
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'O(max(input))',
        'current_operation': 'Putting everyone to sleep...',
        'elements_awake': 0
    }
    
    start_time = time.time()
    input_data = sorted(data) # We cheat to simulate the "wake up" order in a single-threaded generator
    arr = []
    
    yield arr.copy(), stats.copy()
    
    for val in input_data:
        # Simulate wait time proportional to value
        wait_time = val * scale_factor
        stats['current_operation'] = f'Waiting for {val} to wake up... (Estimated {wait_time:.2f}s)'
        
        # In a real visualizer, we want to see progress
        # So we sleep in small increments
        elapsed_inc = 0
        while elapsed_inc < wait_time:
            sleep_inc = min(0.1, wait_time - elapsed_inc)
            if delay > 0: time.sleep(sleep_inc)
            elapsed_inc += sleep_inc
            stats['time_elapsed'] = time.time() - start_time
            yield arr.copy(), stats.copy()
            
        arr.append(val)
        stats['elements_awake'] += 1
        stats['current_operation'] = f'Element {val} has woken up!'
        stats['time_elapsed'] = time.time() - start_time
        yield arr.copy(), stats.copy()
    
    stats['current_operation'] = '[DONE] Everyone is awake and sorted.'
    yield arr, stats
