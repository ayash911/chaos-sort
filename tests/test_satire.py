import unittest
from tests.base_test import BaseSortTest
from chaos_sort import satire

class TestSatireSorts(BaseSortTest):
    """Test suite for satirical sorting algorithms."""
    
    def test_thanos_sort(self):
        # Thanos sort removes elements until sorted
        data = [5, 2, 8, 1, 9]
        result = self.run_sort(satire.thanos_sort, data)
        self.assert_sorted(result)
        self.assertTrue(len(result) <= 5)

    def test_gaslight_sort(self):
        self.run_standard_checks(satire.gaslight_sort)

    def test_bureaucracy_sort(self):
        self.run_standard_checks(satire.bureaucracy_sort, delay=0.0)

    def test_stackoverflow_sort(self):
        self.run_standard_checks(satire.stackoverflow_sort)

    def test_trust_fund_sort(self):
        self.run_standard_checks(satire.trust_fund_sort)

    def test_genz_sort(self):
        # Gen Z sort deletes "bad vibes"
        data = [50, 10, 80, 20]
        result = self.run_sort(satire.genz_sort, data)
        # We don't assert sorted here if vibes are random, 
        # but my implementation just deletes values above threshold.
        # Survived values might still be unsorted.
        pass

    def test_symbolic_sorts(self):
        """Test sorts that don't actually sort but should run without error."""
        data = [3, 1, 2]
        satire.politician_sort(data.copy())
        satire.procrastination_sort(data.copy())
        satire.intimidation_sort(data.copy())
        satire.lottery_sort(data.copy())
        satire.philosophical_sort(data.copy())

if __name__ == "__main__":
    unittest.main()
