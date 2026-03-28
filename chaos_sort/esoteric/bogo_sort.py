"""
chaos_sort.esoteric.bogo_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Bogo Sort (Permutation Sort, Stupid Sort) using generator-based execution.

Time Complexity: O((n+1)!) average, O(∞) worst case
Space Complexity: O(1)
Stable: No
Status: Hilariously inefficient
"""

import time
import random
from typing import List, Dict, Generator, Tuple, Any


def bogo_sort(
    data: List[int],
    delay: float = 0.0,
    entropy_mode: str = "true_random",
    max_iterations: int = 1000000,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Bogo Sort - Randomly shuffle until sorted.
    
    The "sorting" algorithm that works by repeatedly shuffling the array
    randomly until, by pure chance, it ends up sorted. Expected time is
    factorial, making it one of the worst sorting algorithms ever conceived.
    
    Named after the Bogosort algorithm, popularized in the 1980s as an
    example of what NOT to do in algorithm design.
    
    Parameters
    ----------
    data : List[int]
        The array to sort
    delay : float, optional
        Artificial delay between shuffles for visualization (default: 0.0)
    entropy_mode : str, optional
        Randomness source: 'true_random', 'pseudo_random', 'cosmic_rays' (default: 'true_random')
        Note: 'cosmic_rays' just adds dramatic text, doesn't actually use cosmic rays
    max_iterations : int, optional
        Maximum number of shuffles before giving up (default: 1,000,000)
    **kwargs
        Additional parameters (ignored for this algorithm)
        
    Yields
    ------
    Tuple[List[int], Dict[str, Any]]
        Current state of the array and statistics dictionary
        
    Warnings
    --------
    This algorithm has O((n+1)!) average time complexity.
    For arrays larger than 10 elements, you may be waiting a VERY long time.
    Seriously. Don't use this for actual sorting.
    
    Examples
    --------
    >>> data = [3, 1, 2]  # Keep it small!
    >>> for array, stats in bogo_sort(data, max_iterations=100):
    ...     if stats['comparisons'] % 10 == 0:
    ...         print(f"Attempt {stats['comparisons']}: {array}")
    """
    
    # Initialize statistics
    stats = {
        'comparisons': 0,
        'swaps': 0,  # Each shuffle counts as n swaps
        'time_elapsed': 0.0,
        'theoretical_time': _calculate_theoretical_time(len(data)),
        'current_operation': 'Praying to RNG gods...'
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    
    # Yield initial state
    yield arr.copy(), stats.copy()
    
    def is_sorted(arr: List[int]) -> bool:
        """Check if array is sorted."""
        nonlocal stats
        stats['comparisons'] += n - 1  # n-1 comparisons to verify
        return all(arr[i] <= arr[i + 1] for i in range(n - 1))
    
    # The actual "algorithm"
    iteration = 0
    while not is_sorted(arr) and iteration < max_iterations:
        iteration += 1
        
        # Shuffle the array randomly
        if entropy_mode == "cosmic_rays":
            stats['current_operation'] = f'Attempt #{iteration}: Awaiting cosmic ray bit-flip...'
        else:
            stats['current_operation'] = f'Attempt #{iteration}: Shuffling randomly...'
        
        random.shuffle(arr)
        stats['swaps'] += n  # Shuffle involves approximately n swaps
        stats['time_elapsed'] = time.time() - start_time
        
        if delay > 0:
            time.sleep(delay)
        
        yield arr.copy(), stats.copy()
        
        # Every 100 iterations, add some flavor text
        if iteration % 100 == 0:
            stats['current_operation'] = f'Attempt #{iteration}: Still not sorted. Maybe next time?'
            yield arr.copy(), stats.copy()
    
    # Check if we succeeded or gave up
    if is_sorted(arr):
        stats['current_operation'] = f'[SORTED] after {iteration} random shuffles!'
    else:
        stats['current_operation'] = f'[WARNING] Gave up after {max_iterations} attempts. This is taking too long.'
    
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats


def _calculate_theoretical_time(n: int) -> str:
    """
    Calculate the expected time for Bogo Sort to complete.
    
    Returns a humorous string describing the astronomical time required.
    """
    import math
    
    if n <= 5:
        return "A few seconds (if lucky)"
    elif n <= 10:
        return "Hours to days (pray harder)"
    elif n <= 15:
        return "Centuries (don't hold your breath)"
    else:
        # Factorial grows FAST
        factorial = math.factorial(n)
        
        # Assume 1 million shuffles per second
        seconds = factorial / 1_000_000
        
        # Convert to cosmic timescales
        age_of_universe = 13.8e9 * 365.25 * 24 * 3600  # seconds
        
        if seconds > age_of_universe * 1e100:
            return f"Heat death of the universe × 10^100 (factorial is {factorial:.2e})"
        elif seconds > age_of_universe:
            universes = seconds / age_of_universe
            return f"{universes:.2e} times the age of the universe"
        else:
            years = seconds / (365.25 * 24 * 3600)
            return f"~{years:.2e} years"


# Variant: Bozo Sort (swap two random elements instead of full shuffle)
def bozo_sort(
    data: List[int],
    delay: float = 0.0,
    max_iterations: int = 1000000,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Bozo Sort - Like Bogo Sort, but even more inefficient.
    
    Instead of shuffling the entire array, randomly swap two elements
    and check if it's sorted. Repeat until sorted (or heat death).
    
    Time Complexity: O(n·n!) average case
    
    Parameters
    ----------
    data : List[int]
        The array to sort
    delay : float, optional
        Delay between swaps (default: 0.0)
    max_iterations : int, optional
        Maximum swaps before giving up (default: 1,000,000)
    """
    
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': f"Worse than Bogo Sort by a factor of n",
        'current_operation': 'Randomly swapping elements...'
    }
    
    start_time = time.time()
    arr = data.copy()
    n = len(arr)
    
    yield arr.copy(), stats.copy()
    
    def is_sorted(arr: List[int]) -> bool:
        """Check if sorted."""
        nonlocal stats
        stats['comparisons'] += n - 1
        return all(arr[i] <= arr[i + 1] for i in range(n - 1))
    
    iteration = 0
    while not is_sorted(arr) and iteration < max_iterations:
        iteration += 1
        
        # Pick two random indices and swap
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
        stats['swaps'] += 1
        stats['current_operation'] = f'Swap #{iteration}: positions {i} ↔ {j}'
        stats['time_elapsed'] = time.time() - start_time
        
        if delay > 0:
            time.sleep(delay)
        
        yield arr.copy(), stats.copy()
    
    if is_sorted(arr):
        stats['current_operation'] = f'[SORTED] Somehow sorted after {iteration} random swaps!'
    else:
        stats['current_operation'] = f'[WARNING] Gave up. Still not sorted.'
    
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats


# Example usage
if __name__ == "__main__":
    # Test with a SMALL array (seriously, keep it small)
    test_data = [5, 2, 8, 1, 9]
    print(f"Original: {test_data}")
    print(f"Expected attempts for {len(test_data)} elements: ~{120} (5!)")
    print("\nStarting Bogo Sort...")
    print("=" * 50)
    
    attempt_count = 0
    for array, stats in bogo_sort(test_data.copy(), max_iterations=10000):
        attempt_count += 1
        if attempt_count % 50 == 0:
            print(f"Attempt {attempt_count}: {array} | Time: {stats['time_elapsed']:.2f}s")
        
        # Stop early if sorted
        if stats['current_operation'].startswith('[SORTED]'):
            print(f"\n[SUCCESS]! Sorted after {attempt_count} attempts!")
            print(f"Final: {array}")
            print(f"Time: {stats['time_elapsed']:.4f}s")
            break
    else:
        print(f"\n[FAILED] to sort after {attempt_count} attempts.")
        print(f"Final state: {array}")