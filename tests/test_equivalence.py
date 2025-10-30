"""
Tests comparing slow vs optimized implementations.
Ensures both produce identical results.
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import slow_code_examples as slow
import optimized_code as fast


class TestEquivalence:
    """Tests that verify slow and optimized versions produce same results."""
    
    def test_string_concatenation_equivalence(self):
        items = ["test", "items", "here"]
        slow_result = slow.inefficient_string_concatenation(items, 5)
        fast_result = fast.optimized_string_concatenation(items, 5)
        assert slow_result == fast_result
    
    def test_list_search_equivalence(self):
        data = list(range(100))
        searches = [10, 50, 99, 150]
        slow_result = slow.inefficient_list_search(data, searches)
        fast_result = fast.optimized_list_search(data, searches)
        assert slow_result == fast_result
    
    def test_list_comprehension_equivalence(self):
        for n in [10, 50, 100]:
            slow_result = slow.inefficient_list_comprehension(n)
            fast_result = fast.optimized_list_comprehension(n)
            assert slow_result == fast_result
    
    def test_dictionary_operations_equivalence(self):
        items = [("a", 1), ("b", 2), ("a", 3), ("b", 4), ("c", 5)]
        slow_result = slow.inefficient_dictionary_operations(items)
        fast_result = fast.optimized_dictionary_operations(items)
        assert slow_result == fast_result
    
    def test_duplicate_removal_equivalence(self):
        items = [1, 2, 3, 2, 4, 1, 5, 3]
        slow_result = slow.inefficient_duplicate_removal(items)
        fast_result = fast.optimized_duplicate_removal(items)
        assert slow_result == fast_result
    
    def test_sum_calculation_equivalence(self):
        numbers = list(range(100))
        slow_result = slow.inefficient_sum_calculation(numbers)
        fast_result = fast.optimized_sum_calculation(numbers)
        assert slow_result == fast_result
    
    def test_fibonacci_equivalence(self):
        # Test smaller values to avoid exponential time in slow version
        for n in range(15):
            slow_result = slow.inefficient_recursive_fibonacci(n)
            fast_result = fast.optimized_recursive_fibonacci(n)
            fast_iter_result = fast.optimized_fibonacci_iterative(n)
            assert slow_result == fast_result == fast_iter_result
    
    def test_matrix_multiplication_equivalence(self):
        m1 = [[1, 2, 3], [4, 5, 6]]
        m2 = [[7, 8], [9, 10], [11, 12]]
        slow_result = slow.inefficient_nested_loops(m1, m2)
        fast_result = fast.optimized_nested_loops(m1, m2)
        assert slow_result == fast_result
    
    def test_data_filtering_equivalence(self):
        data = [
            {'id': i, 'value': i * 10}
            for i in range(20)
        ]
        threshold = 100
        slow_result = slow.inefficient_data_filtering(data, threshold)
        fast_result = fast.optimized_data_filtering(data, threshold)
        assert slow_result == fast_result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
