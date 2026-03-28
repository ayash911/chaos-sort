"""
Standard Sorting Algorithms
============================

Classic, well-known sorting algorithms used in production systems.
These serve as baselines for comparison with the more exotic algorithms.

Available Algorithms:
- bubble_sort: O(n²) - Simple adjacent swaps
- selection_sort: O(n²) - Find minimum iteratively
- insertion_sort: O(n²) - Build sorted array one by one
- merge_sort: O(n log n) - Divide and conquer
- quick_sort: O(n log n) - Recursive partitioning
- heap_sort: O(n log n) - Binary heap structure
- radix_sort: O(nk) - Non-comparative digit sort
- counting_sort: O(n+k) - Count occurrences
- shell_sort: O(n log n) - Optimized insertion sort
- cocktail_sort: O(n²) - Bidirectional bubble sort
"""

from chaos_sort.standards.bubble_sort import bubble_sort
from chaos_sort.standards.selection_sort import selection_sort
from chaos_sort.standards.insertion_sort import insertion_sort
from chaos_sort.standards.merge_sort import merge_sort
from chaos_sort.standards.quick_sort import quick_sort
from chaos_sort.standards.heap_sort import heap_sort
from chaos_sort.standards.radix_sort import radix_sort
from chaos_sort.standards.counting_sort import counting_sort
from chaos_sort.standards.shell_sort import shell_sort
from chaos_sort.standards.cocktail_sort import cocktail_sort

__all__ = [
    'bubble_sort',
    'selection_sort',
    'insertion_sort',
    'merge_sort',
    'quick_sort',
    'heap_sort',
    'radix_sort',
    'counting_sort',
    'shell_sort',
    'cocktail_sort',
]