"""
chaos_sort.standards.cocktail_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Cocktail Shaker Sort using generator-based execution for visualization.

Time Complexity: O(n²)
Space Complexity: O(1)
Stable: Yes
"""

import time
from typing import List, Dict, Generator, Tuple, Any


def cocktail_sort(
    data: List[int],
    delay: float = 0.0,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Cocktail Shaker Sort - Variation of bubble sort that sorts in both directions.
    
    Parameters
    ----------
    data : List[int]
        The array to sort
    delay : float, optional
        Artificial delay between operations for visualization (default: 0.0)
    **kwargs
        Additional parameters
        
    Yields
    ------
    Tuple[List[int], Dict[str, Any]]
        Current state of the array and statistics dictionary
    """
    
    # Initialize statistics
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'O(n^2)',
        'current_operation': 'Starting Cocktail Sort'
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    
    # Yield initial state
    yield arr.copy(), stats.copy()
    
    swapped = True
    start = 0
    end = n - 1
    
    while swapped:
        swapped = False
        
        # Forward pass: like bubble sort
        for i in range(start, end):
            stats['comparisons'] += 1
            stats['current_operation'] = f'Forward pass: comparing [{i}] and [{i+1}]'
            stats['time_elapsed'] = time.time() - start_time
            yield arr.copy(), stats.copy()
            
            if delay > 0:
                time.sleep(delay * 0.5)
            
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                stats['swaps'] += 1
                swapped = True
                yield arr.copy(), stats.copy()
                if delay > 0:
                    time.sleep(delay * 0.5)
        
        if not swapped:
            break
            
        swapped = False
        end -= 1
        
        # Backward pass
        for i in range(end - 1, start - 1, -1):
            stats['comparisons'] += 1
            stats['current_operation'] = f'Backward pass: comparing [{i}] and [{i+1}]'
            stats['time_elapsed'] = time.time() - start_time
            yield arr.copy(), stats.copy()
            
            if delay > 0:
                time.sleep(delay * 0.5)
                
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                stats['swaps'] += 1
                swapped = True
                yield arr.copy(), stats.copy()
                if delay > 0:
                    time.sleep(delay * 0.5)
                    
        start += 1
        
    # Final state
    stats['current_operation'] = 'Complete'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
