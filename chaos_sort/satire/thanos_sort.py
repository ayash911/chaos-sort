"""
chaos_sort.satire.thanos_sort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Thanos Sort - Because perfectly balanced, as all things should be.

Time Complexity: O(n log n) [by elimination]
Space Complexity: O(1) [technically correct - less space after each snap]
Stable: Extremely unstable
Ethical: Questionable
"""

import time
import random
from typing import List, Dict, Generator, Tuple, Any


def thanos_sort(
    data: List[int],
    delay: float = 0.1,
    destructive_allowed: bool = True,
    snap_quota: float = 0.5,
    show_mercy: bool = False,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Thanos Sort - Perfectly balanced, as all things should be.
    
    Inspired by the Mad Titan himself, this algorithm achieves "sortedness"
    by randomly eliminating exactly half the elements until the remaining
    elements happen to be in sorted order.
    
    The algorithm works as follows:
    1. Check if array is sorted
    2. If not, snap away half the elements (chosen randomly)
    3. Repeat until sorted or only one element remains
    
    "I am inevitable. And so is O(log n) if you just delete enough data."
                                                        - Thanos, probably
    
    Parameters
    ----------
    data : List[int]
        The array to sort (and decimate)
    delay : float, optional
        Dramatic pause between each snap (default: 0.1s for maximum drama)
    destructive_allowed : bool, optional
        Must be True or the algorithm refuses to run (default: True)
    snap_quota : float, optional
        Fraction of elements to eliminate per snap (default: 0.5 for perfect balance)
    show_mercy : bool, optional
        If True, tries to keep the smallest/largest elements (default: False)
    **kwargs
        Additional parameters (ignored)
        
    Yields
    ------
    Tuple[List[int], Dict[str, Any]]
        Current state of the array and statistics dictionary
        
    Warnings
    --------
    This algorithm DESTROYS DATA. It does not actually sort; it eliminates
    elements until what remains is sorted. Use only for educational purposes
    and dramatic effect.
    
    Notes
    -----
    "Fun isn't something one considers when balancing the universe. But this...
    does put a smile on my face." - Thanos
    
    Examples
    --------
    >>> data = [64, 25, 12, 22, 11]
    >>> for array, stats in thanos_sort(data):
    ...     print(f"Remaining: {array} | Snapped: {stats['elements_eliminated']}")
    """
    
    if not destructive_allowed:
        raise ValueError(
            "Thanos Sort requires destructive_allowed=True. "
            "You cannot achieve balance without sacrifice."
        )
    
    # Initialize statistics
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': "O(n log n) but at what cost?",
        'current_operation': 'Collecting the Infinity Stones...',
        'snap_count': 0,
        'elements_eliminated': 0,
        'original_size': len(data),
        'destiny_fulfilled': False
    }
    
    start_time = time.time()
    arr = data.copy()
    original_elements = set(arr)  # Remember who we lost
    
    # Yield initial state
    yield arr.copy(), stats.copy()
    
    def is_sorted(arr: List[int]) -> bool:
        """Check if array is sorted."""
        if len(arr) <= 1:
            return True
        nonlocal stats
        stats['comparisons'] += len(arr) - 1
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    
    # The Snappening
    while len(arr) > 1 and not is_sorted(arr):
        stats['snap_count'] += 1
        pre_snap_size = len(arr)
        
        # Calculate how many to eliminate
        n_to_eliminate = max(1, int(len(arr) * snap_quota))
        
        # Dramatic buildup
        stats['current_operation'] = f'Snap #{stats["snap_count"]}: Raising the Gauntlet...'
        stats['time_elapsed'] = time.time() - start_time
        yield arr.copy(), stats.copy()
        
        if delay > 0:
            time.sleep(delay * 0.5)
        
        # THE SNAP
        if show_mercy:
            # Show mercy to extremes (keep smallest and largest more likely)
            sorted_indices = sorted(range(len(arr)), key=lambda i: arr[i])
            # Eliminate from the middle
            middle_indices = sorted_indices[len(sorted_indices)//4:-len(sorted_indices)//4]
            indices_to_remove = random.sample(
                middle_indices if len(middle_indices) >= n_to_eliminate else list(range(len(arr))),
                min(n_to_eliminate, len(arr) - 1)
            )
        else:
            # Perfectly balanced - pure random selection
            indices_to_remove = random.sample(range(len(arr)), min(n_to_eliminate, len(arr) - 1))
        
        # Remove elements (in reverse order to maintain indices)
        eliminated_values = []
        for idx in sorted(indices_to_remove, reverse=True):
            eliminated_values.append(arr.pop(idx))
        
        stats['elements_eliminated'] += len(eliminated_values)
        stats['current_operation'] = (
            f'[SNAP] Snap #{stats["snap_count"]}: Eliminated {len(eliminated_values)} elements. '
            f'Remaining: {len(arr)}/{stats["original_size"]}'
        )
        stats['time_elapsed'] = time.time() - start_time
        
        if delay > 0:
            time.sleep(delay)
        
        yield arr.copy(), stats.copy()
        
        # Flavor text every few snaps
        if stats['snap_count'] % 3 == 0 and len(arr) > 1:
            stats['current_operation'] = f'"Perfectly balanced..." - Remaining: {len(arr)} elements'
            yield arr.copy(), stats.copy()
    
    # Check final state
    if is_sorted(arr):
        survival_rate = (len(arr) / stats['original_size']) * 100
        stats['destiny_fulfilled'] = True
        stats['current_operation'] = (
            f'[BALANCED]: {len(arr)}/{stats["original_size"]} elements survived ({survival_rate:.1f}%). '
            f'Array is now sorted. Cost: {stats["elements_eliminated"]} souls.'
        )
    elif len(arr) == 1:
        stats['current_operation'] = (
            f'[WARNING] Only one element remains: {arr[0]}. '
            f'Technically sorted, but at what cost?'
        )
    else:
        stats['current_operation'] = 'This... does not put a smile on my face.'
    
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats


# Bonus variant: Infinity Gauntlet Sort
def infinity_gauntlet_sort(
    data: List[int],
    delay: float = 0.15,
    **kwargs
) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Infinity Gauntlet Sort - Use all six stones for maximum efficiency.
    
    This variant uses different "stones" for different operations:
    - Reality Stone: Change values to make them sorted
    - Time Stone: Just claim it was always sorted
    - Space Stone: Rearrange elements across the array
    - Power Stone: Delete elements (like Thanos Sort)
    - Mind Stone: Convince the user it's sorted
    - Soul Stone: Requires a sacrifice (deletes the smallest element first)
    
    Randomly picks a stone for each operation.
    """
    
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'time_elapsed': 0.0,
        'theoretical_time': 'All of time and space',
        'current_operation': 'Assembling the Infinity Gauntlet...',
        'stones_used': []
    }
    
    start_time = time.time()
    arr = data.copy()
    
    yield arr.copy(), stats.copy()
    
    stones = [
        "Reality Stone: Altering values",
        "Time Stone: Reversing entropy", 
        "Space Stone: Teleporting elements",
        "Power Stone: Obliterating chaos",
        "Mind Stone: Controlling perception",
        "Soul Stone: Demanding sacrifice"
    ]
    
    # Just use Thanos Sort but with dramatic stone names
    snap_count = 0
    while len(arr) > 1 and not all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        snap_count += 1
        stone = random.choice(stones)
        stats['stones_used'].append(stone)
        stats['current_operation'] = f'Using {stone}... Snap #{snap_count}'
        
        # Eliminate half
        n_to_remove = max(1, len(arr) // 2)
        indices_to_remove = random.sample(range(len(arr)), min(n_to_remove, len(arr) - 1))
        
        for idx in sorted(indices_to_remove, reverse=True):
            arr.pop(idx)
        
        if delay > 0:
            time.sleep(delay)
        
        stats['time_elapsed'] = time.time() - start_time
        yield arr.copy(), stats.copy()
    
    stats['current_operation'] = f'[DONE] Gauntlet complete! {len(arr)} elements remain.'
    stats['time_elapsed'] = time.time() - start_time
    yield arr, stats


# Example usage
if __name__ == "__main__":
    # Test data
    test_data = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 23, 36, 77, 99, 15, 42]
    print(f"Original array ({len(test_data)} elements): {test_data}")
    print("\nInitiating Thanos Sort...")
    print("=" * 70)
    print('"Fun isn\'t something one considers when balancing the universe..."')
    print("=" * 70)
    print()
    
    for array, stats in thanos_sort(test_data.copy(), delay=0.2):
        if 'Snap' in stats['current_operation'] or 'BALANCED' in stats['current_operation']:
            print(f"{stats['current_operation']}")
            print(f"  Array: {array}")
            print()
    
    print("=" * 70)
    print(f"Final Statistics:")
    print(f"  Snaps required: {stats['snap_count']}")
    print(f"  Elements eliminated: {stats['elements_eliminated']}")
    print(f"  Survival rate: {len(array)}/{stats['original_size']} "
          f"({len(array)/stats['original_size']*100:.1f}%)")
    print(f"  Time elapsed: {stats['time_elapsed']:.4f}s")
    print(f"  Destiny fulfilled: {stats['destiny_fulfilled']}")
    print("=" * 70)