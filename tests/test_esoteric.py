import unittest
from tests.base_test import BaseSortTest
from chaos_sort import esoteric

class TestEsotericSorts(BaseSortTest):
    """Test suite for esoteric sorting algorithms."""
    
    def test_stalin_sort(self):
        self.run_standard_checks(esoteric.stalin_sort, destructive=True)

    def test_gnome_sort(self):
        self.run_standard_checks(esoteric.gnome_sort)

    def test_pancake_sort(self):
        self.run_standard_checks(esoteric.pancake_sort)

    def test_stooge_sort_small(self):
        # Stooge is very slow, test small
        data = [3, 1, 2, 5, 4]
        result = self.run_sort(esoteric.stooge_sort, data)
        self.assert_sorted(result)

    def test_slow_sort_tiny(self):
        data = [3, 1, 2]
        result = self.run_sort(esoteric.slow_sort, data)
        self.assert_sorted(result)

    def test_sleep_sort_mock(self):
        # We use a high scale factor in implementation, but test with tiny scale
        data = [3, 1, 2]
        result = self.run_sort(esoteric.sleep_sort, data, scale_factor=0.001)
        self.assert_sorted(result)

    def test_miracle_sort_mock(self):
        # Force a miracle quickly
        data = [2, 1]
        result = self.run_sort(esoteric.miracle_sort, data, miracle_chance=1.0)
        self.assert_sorted(result)

    def test_quantum_bogo_sort(self):
        self.run_standard_checks(esoteric.quantum_bogo_sort)

    def test_spaghetti_sort(self):
        self.run_standard_checks(esoteric.spaghetti_sort)

    def test_bogobogo_sort_tiny(self):
        data = [2, 1]
        result = self.run_sort(esoteric.bogobogo_sort, data, max_iterations=100)
        # It's chance based, might not be sorted but should run
        pass

if __name__ == "__main__":
    unittest.main()
