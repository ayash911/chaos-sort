"""
chaos_sort.standards.merge_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Merge Sort using generator-based execution for visualization.

Time Complexity: O(n log n)
Space Complexity: O(n)
Stable: Yes
"""

import time
from typing import List, Dict, Generator, Tuple, Any


def merge_sort(
    data: List[int],
    delay: float = 0.0,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Merge Sort - A classic divide-and-conquer sorting algorithm.
    
    Recursively divides the array into halves, sorts them, and merges
    the sorted halves back together.
    
    Parameters
    ----------
    data : List[int]
        The array to sort
    delay : float, optional
        Artificial delay between operations for visualization (default: 0.0)
    **kwargs
        Additional parameters (ignored for this algorithm)
        
    Yields
    ------
    Tuple[List[int], Dict[str, Any]]
        Current state of the array and statistics dictionary
        
    Examples
    --------
    >>> data = [64, 34, 25, 12, 22, 11, 90]
    >>> for array, stats in merge_sort(data):
    ...     print(f"Comparisons: {stats['comparisons']}, Swaps: {stats['swaps']}")
    """
    
    # Initialize statistics
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': None,
        'current_operation': 'Starting Merge Sort'
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    
    # Yield initial state
    yield arr.copy(), stats.copy()
    
    def merge(arr: List[int], left: int, mid: int, right: int) -> None:
        """Merge two sorted subarrays."""
        nonlocal stats
        
        # Create temporary arrays
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        # Merge the temporary arrays back
        while i < len(left_arr) and j < len(right_arr):
            stats['comparisons'] += 1
            stats['current_operation'] = f'Merging: comparing positions {left + i} and {mid + 1 + j}'
            
            if delay > 0:
                time.sleep(delay)
            
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            
            stats['swaps'] += 1
            stats['time_elapsed'] = time.time() - start_time
            k += 1
        
        # Copy remaining elements
        while i < len(left_arr):
            arr[k] = left_arr[i]
            stats['swaps'] += 1
            stats['current_operation'] = f'Copying remaining from left subarray'
            i += 1
            k += 1
            
            if delay > 0:
                time.sleep(delay)
            stats['time_elapsed'] = time.time() - start_time
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            stats['swaps'] += 1
            stats['current_operation'] = f'Copying remaining from right subarray'
            j += 1
            k += 1
            
            if delay > 0:
                time.sleep(delay)
            stats['time_elapsed'] = time.time() - start_time
    
    def merge_sort_recursive(arr: List[int], left: int, right: int) -> Generator:
        """Recursive merge sort with yields."""
        if left < right:
            mid = (left + right) // 2
            
            stats['current_operation'] = f'Dividing: [{left}:{mid}] and [{mid+1}:{right}]'
            yield arr.copy(), stats.copy()
            
            # Sort first half
            yield from merge_sort_recursive(arr, left, mid)
            
            # Sort second half
            yield from merge_sort_recursive(arr, mid + 1, right)
            
            # Merge the sorted halves
            merge(arr, left, mid, right)
            stats['current_operation'] = f'Merged: [{left}:{right}]'
            yield arr.copy(), stats.copy()
    
    # Execute the recursive merge sort
    yield from merge_sort_recursive(arr, 0, n - 1)
    
    # Final state
    stats['current_operation'] = 'Complete'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats


# Example usage and test
if __name__ == "__main__":
    import random
    
    # Test data
    test_data = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 23, 36]
    print(f"Original: {test_data}")
    
    # Run sorting
    step_count = 0
    for array, stats in merge_sort(test_data.copy()):
        step_count += 1
        if step_count % 5 == 0:  # Print every 5th step
            print(f"Step {step_count}: {array[:8]}... | "
                  f"Comparisons: {stats['comparisons']}, Swaps: {stats['swaps']}")
    
    print(f"\nFinal: {array}")
    print(f"Total Comparisons: {stats['comparisons']}")
    print(f"Total Swaps: {stats['swaps']}")
    print(f"Time: {stats['time_elapsed']:.4f}s")