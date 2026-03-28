import unittest
from tests.base_test import BaseSortTest
from chaos_sort.standards import (
    bubble_sort, selection_sort, insertion_sort, merge_sort,
    quick_sort, heap_sort, radix_sort, counting_sort,
    shell_sort, cocktail_sort
)

class TestStandardSorts(BaseSortTest):
    """Test suite for standard sorting algorithms."""
    
    def test_bubble_sort(self):
        self.run_standard_checks(bubble_sort)

    def test_selection_sort(self):
        self.run_standard_checks(selection_sort)

    def test_insertion_sort(self):
        self.run_standard_checks(insertion_sort)

    def test_merge_sort(self):
        self.run_standard_checks(merge_sort)

    def test_quick_sort(self):
        self.run_standard_checks(quick_sort)

    def test_heap_sort(self):
        self.run_standard_checks(heap_sort)

    def test_radix_sort(self):
        self.run_standard_checks(radix_sort)

    def test_counting_sort(self):
        self.run_standard_checks(counting_sort)

    def test_shell_sort(self):
        self.run_standard_checks(shell_sort)

    def test_cocktail_sort(self):
        self.run_standard_checks(cocktail_sort)

if __name__ == "__main__":
    unittest.main()
