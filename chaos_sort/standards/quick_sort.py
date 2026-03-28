"""
chaos_sort.standards.quick_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Quick Sort using generator-based execution for visualization.

Time Complexity: O(n log n) average, O(n²) worst case
Space Complexity: O(log n)
Stable: No
"""

import time
import random
from typing import List, Dict, Generator, Tuple, Any


def quick_sort(
    data: List[int],
    delay: float = 0.0,
    pivot_strategy: str = "last",
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Quick Sort - A highly efficient sorting algorithm and is based on 
    partitioning of array of data into smaller arrays.
    
    Parameters
    ----------
    data : List[int]
        The array to sort
    delay : float, optional
        Artificial delay between operations for visualization (default: 0.0)
    pivot_strategy : str, optional
        How to choose the pivot: 'first', 'last', 'middle', 'random' (default: 'last')
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
        'theoretical_time': 'O(n log n)',
        'current_operation': 'Starting Quick Sort'
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    
    # Yield initial state
    yield arr.copy(), stats.copy()
    
    def partition(low: int, high: int) -> Generator:
        """Partition the array using the chosen pivot strategy."""
        nonlocal stats
        
        # Select pivot index
        if pivot_strategy == "random":
            pivot_idx = random.randint(low, high)
        elif pivot_strategy == "middle":
            pivot_idx = (low + high) // 2
        elif pivot_strategy == "first":
            pivot_idx = low
        else: # last
            pivot_idx = high
            
        pivot = arr[pivot_idx]
        stats['current_operation'] = f'Partitioning: [{low}:{high}] | Pivot: {pivot} at index [{pivot_idx}]'
        yield arr.copy(), stats.copy()
        
        # Move pivot to the end for standard Lomuto partition if it's not already there
        if pivot_idx != high:
            arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
            stats['swaps'] += 1
            yield arr.copy(), stats.copy()
        
        i = low - 1
        for j in range(low, high):
            stats['comparisons'] += 1
            stats['current_operation'] = f'Comparing: {arr[j]} with pivot {pivot}'
            stats['time_elapsed'] = time.time() - start_time
            yield arr.copy(), stats.copy()
            
            if delay > 0:
                time.sleep(delay * 0.5)
            
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                stats['swaps'] += 1
                stats['current_operation'] = f'Swapping: [{i}] and [{j}]'
                yield arr.copy(), stats.copy()
                
                if delay > 0:
                    time.sleep(delay * 0.5)
        
        # Final swap to put pivot in its correct place
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        stats['swaps'] += 1
        stats['current_operation'] = f'Pivot placed at index [{i+1}]'
        yield arr.copy(), stats.copy()
        
        return i + 1
    
    def qsort_recursive(low: int, high: int) -> Generator:
        """Recursive quick sort with yields."""
        if low < high:
            # pi is partitioning index, arr[p] is now at right place
            pi = yield from partition(low, high)
            
            yield from qsort_recursive(low, pi - 1)
            yield from qsort_recursive(pi + 1, high)
    
    # Execute the recursive quick sort
    yield from qsort_recursive(0, n - 1)
    
    # Final state
    stats['current_operation'] = 'Complete'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats
