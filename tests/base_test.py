import unittest
import random
from typing import List, Callable, Generator, Tuple, Dict, Any

class BaseSortTest(unittest.TestCase):
    """
    Base class for testing sorting algorithms.
    Provides utility methods for testing correctness.
    """
    
    def run_sort(self, sort_func: Callable, data: List[int], **kwargs) -> List[int]:
        """Helper to run a sorting algorithm and return the final state."""
        final_array = data
        for array, stats in sort_func(data.copy(), **kwargs):
            final_array = array
        return final_array

    def assert_sorted(self, array: List[int]):
        """Custom assertion to check if an array is sorted."""
        self.assertEqual(array, sorted(array), f"Array is not sorted: {array}")

    def check_empty_list(self, sort_func: Callable, **kwargs):
        data = []
        result = self.run_sort(sort_func, data, **kwargs)
        self.assertEqual(result, [])

    def check_single_element(self, sort_func: Callable, **kwargs):
        data = [42]
        result = self.run_sort(sort_func, data, **kwargs)
        self.assertEqual(result, [42])

    def check_already_sorted(self, sort_func: Callable, **kwargs):
        data = [1, 2, 3, 4, 5]
        result = self.run_sort(sort_func, data, **kwargs)
        self.assert_sorted(result)

    def check_reverse_sorted(self, sort_func: Callable, **kwargs):
        data = [5, 4, 3, 2, 1]
        result = self.run_sort(sort_func, data, **kwargs)
        self.assert_sorted(result)

    def check_random_large(self, sort_func: Callable, size: int = 100, destructive: bool = False, **kwargs):
        data = [random.randint(0, 1000) for _ in range(size)]
        result = self.run_sort(sort_func, data, **kwargs)
        self.assert_sorted(result)
        # Verify no elements were lost (for non-destructive sorts)
        if not destructive:
            self.assertEqual(sorted(data), sorted(result))

    def check_duplicates(self, sort_func: Callable, destructive: bool = False, **kwargs):
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = self.run_sort(sort_func, data, **kwargs)
        self.assert_sorted(result)
        if not destructive:
            self.assertEqual(sorted(data), sorted(result))

    def run_standard_checks(self, sort_func: Callable, destructive: bool = False, **kwargs):
        """Run all standard test cases for a sorting algorithm."""
        self.check_empty_list(sort_func, **kwargs)
        self.check_single_element(sort_func, **kwargs)
        self.check_already_sorted(sort_func, **kwargs)
        self.check_reverse_sorted(sort_func, **kwargs)
        self.check_random_large(sort_func, destructive=destructive, **kwargs)
        self.check_duplicates(sort_func, destructive=destructive, **kwargs)
