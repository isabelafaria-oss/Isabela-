"""
Unit tests for optimized code.
Ensures optimized versions produce same results as slow versions.
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import optimized_code as fast


class TestStringConcatenation:
    def test_basic_concatenation(self):
        items = ["a", "b", "c"]
        result = fast.optimized_string_concatenation(items, 1)
        assert "a," in result and "b," in result and "c," in result
    
    def test_empty_list(self):
        result = fast.optimized_string_concatenation([], 1)
        assert result == ""


class TestListSearch:
    def test_found_items(self):
        data = [1, 2, 3, 4, 5]
        search = [2, 4]
        result = fast.optimized_list_search(data, search)
        assert result == [True, True]
    
    def test_not_found_items(self):
        data = [1, 2, 3]
        search = [10, 20]
        result = fast.optimized_list_search(data, search)
        assert result == [False, False]
    
    def test_mixed_results(self):
        data = [1, 2, 3, 4, 5]
        search = [2, 10, 4]
        result = fast.optimized_list_search(data, search)
        assert result == [True, False, True]


class TestListComprehension:
    def test_filters_and_squares(self):
        result = fast.optimized_list_comprehension(20)
        assert result == [144, 196, 256, 324]
    
    def test_small_range(self):
        result = fast.optimized_list_comprehension(10)
        assert result == []


class TestDictionaryOperations:
    def test_aggregation(self):
        items = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]
        result = fast.optimized_dictionary_operations(items)
        assert result == {"a": 4, "b": 6}
    
    def test_single_values(self):
        items = [("x", 10), ("y", 20), ("z", 30)]
        result = fast.optimized_dictionary_operations(items)
        assert result == {"x": 10, "y": 20, "z": 30}


class TestDuplicateRemoval:
    def test_removes_duplicates(self):
        items = [1, 2, 2, 3, 3, 3, 4]
        result = fast.optimized_duplicate_removal(items)
        assert result == [1, 2, 3, 4]
    
    def test_preserves_order(self):
        items = [3, 1, 2, 1, 3]
        result = fast.optimized_duplicate_removal(items)
        assert result == [3, 1, 2]
    
    def test_no_duplicates(self):
        items = [1, 2, 3, 4]
        result = fast.optimized_duplicate_removal(items)
        assert result == [1, 2, 3, 4]


class TestSumCalculation:
    def test_basic_sum(self):
        numbers = [1, 2, 3, 4, 5]
        result = fast.optimized_sum_calculation(numbers)
        assert result == 15
    
    def test_empty_list(self):
        result = fast.optimized_sum_calculation([])
        assert result == 0
    
    def test_negative_numbers(self):
        numbers = [-1, -2, 3, 4]
        result = fast.optimized_sum_calculation(numbers)
        assert result == 4


class TestFibonacci:
    def test_memoized_base_cases(self):
        assert fast.optimized_recursive_fibonacci(0) == 0
        assert fast.optimized_recursive_fibonacci(1) == 1
    
    def test_memoized_values(self):
        assert fast.optimized_recursive_fibonacci(5) == 5
        assert fast.optimized_recursive_fibonacci(10) == 55
        assert fast.optimized_recursive_fibonacci(30) == 832040
    
    def test_iterative_base_cases(self):
        assert fast.optimized_fibonacci_iterative(0) == 0
        assert fast.optimized_fibonacci_iterative(1) == 1
    
    def test_iterative_values(self):
        assert fast.optimized_fibonacci_iterative(5) == 5
        assert fast.optimized_fibonacci_iterative(10) == 55
        assert fast.optimized_fibonacci_iterative(30) == 832040
    
    def test_both_methods_agree(self):
        for n in range(20):
            assert fast.optimized_recursive_fibonacci(n) == fast.optimized_fibonacci_iterative(n)


class TestMatrixMultiplication:
    def test_2x2_matrices(self):
        m1 = [[1, 2], [3, 4]]
        m2 = [[5, 6], [7, 8]]
        result = fast.optimized_nested_loops(m1, m2)
        assert result == [[19, 22], [43, 50]]
    
    def test_identity_matrix(self):
        m1 = [[1, 2], [3, 4]]
        identity = [[1, 0], [0, 1]]
        result = fast.optimized_nested_loops(m1, identity)
        assert result == m1


class TestDataFiltering:
    def test_filters_and_sorts(self):
        data = [
            {'id': 1, 'value': 50},
            {'id': 2, 'value': 150},
            {'id': 3, 'value': 100},
            {'id': 4, 'value': 200},
            {'id': 5, 'value': 75}
        ]
        result = fast.optimized_data_filtering(data, 100)
        assert len(result) == 2
        assert result[0]['value'] == 150
        assert result[1]['value'] == 200
    
    def test_empty_result(self):
        data = [{'id': 1, 'value': 50}, {'id': 2, 'value': 75}]
        result = fast.optimized_data_filtering(data, 100)
        assert result == []


class TestBatchProcessing:
    def test_batch_processing(self):
        data = list(range(-10, 20))
        result = fast.optimized_batch_processing(data, batch_size=5)
        # Should double positive numbers
        expected = [x * 2 for x in data if x > 0]
        assert result == expected
    
    def test_all_negative(self):
        data = list(range(-10, 0))
        result = fast.optimized_batch_processing(data, batch_size=3)
        assert result == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
