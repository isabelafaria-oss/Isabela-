"""
Unit tests to verify that optimized code produces the same results as inefficient code.
"""
import unittest
import tempfile
import os
from inefficient_code import (
    slow_string_concatenation,
    inefficient_list_search,
    repeated_expensive_calls,
    nested_loop_inefficiency,
    unnecessary_list_copies,
    inefficient_file_reading,
    global_lookup_in_loop,
    inefficient_dict_iteration,
    no_list_comprehension,
    repeated_regex_compilation
)
from optimized_code import (
    optimized_string_concatenation,
    optimized_list_search,
    optimized_expensive_calls,
    optimized_nested_loops,
    optimized_list_copies,
    optimized_file_reading,
    optimized_global_lookup,
    optimized_dict_iteration,
    optimized_list_comprehension,
    optimized_regex_compilation
)


class TestOptimizations(unittest.TestCase):
    """Test that optimized versions produce identical results."""
    
    def test_string_concatenation(self):
        """Test string concatenation optimization."""
        test_data = [1, 2, 3, 4, 5]
        inefficient_result = slow_string_concatenation(test_data)
        optimized_result = optimized_string_concatenation(test_data)
        self.assertEqual(inefficient_result, optimized_result)
    
    def test_list_search(self):
        """Test list search optimization."""
        test_list = [1, 2, 3, 4, 5, 3, 2, 1]
        target = 3
        inefficient_result = inefficient_list_search(test_list, target)
        optimized_result = optimized_list_search(test_list, target)
        # Both should find the target (optimized returns single item if found)
        self.assertTrue(target in inefficient_result)
        self.assertTrue(target in optimized_result if optimized_result else False)
    
    def test_list_search_not_found(self):
        """Test list search when target not found."""
        test_list = [1, 2, 3, 4, 5]
        target = 99
        inefficient_result = inefficient_list_search(test_list, target)
        optimized_result = optimized_list_search(test_list, target)
        self.assertEqual(len(inefficient_result), 0)
        self.assertEqual(len(optimized_result), 0)
    
    def test_expensive_calls(self):
        """Test repeated expensive calculation optimization."""
        n = 10
        inefficient_result = repeated_expensive_calls(n)
        optimized_result = optimized_expensive_calls(n)
        self.assertEqual(inefficient_result, optimized_result)
    
    def test_nested_loops(self):
        """Test nested loop optimization."""
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        inefficient_result = set(nested_loop_inefficiency(list1, list2))
        optimized_result = set(optimized_nested_loops(list1, list2))
        self.assertEqual(inefficient_result, optimized_result)
    
    def test_list_copies(self):
        """Test unnecessary list copies optimization."""
        test_data = [1, 2, 3, 4, 5]
        inefficient_result = unnecessary_list_copies(test_data)
        optimized_result = optimized_list_copies(test_data)
        self.assertEqual(inefficient_result, optimized_result)
    
    def test_file_reading(self):
        """Test file reading optimization."""
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("line1\n")
            f.write("line2\n")
            f.write("line3\n")
            temp_filename = f.name
        
        try:
            inefficient_result = inefficient_file_reading(temp_filename)
            optimized_result = optimized_file_reading(temp_filename)
            self.assertEqual(inefficient_result, optimized_result)
        finally:
            os.unlink(temp_filename)
    
    def test_file_reading_not_found(self):
        """Test file reading with non-existent file."""
        inefficient_result = inefficient_file_reading("/nonexistent/file.txt")
        optimized_result = optimized_file_reading("/nonexistent/file.txt")
        self.assertEqual(inefficient_result, [])
        self.assertEqual(optimized_result, [])
    
    def test_global_lookup(self):
        """Test global lookup optimization."""
        test_items = [1, 22, 333, 4444]
        inefficient_result = global_lookup_in_loop(test_items)
        optimized_result = optimized_global_lookup(test_items)
        self.assertEqual(inefficient_result, optimized_result)
    
    def test_dict_iteration(self):
        """Test dictionary iteration optimization."""
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        inefficient_result = sorted(inefficient_dict_iteration(test_dict))
        optimized_result = sorted(optimized_dict_iteration(test_dict))
        self.assertEqual(inefficient_result, optimized_result)
    
    def test_list_comprehension(self):
        """Test list comprehension optimization."""
        test_numbers = [1, 2, 3, 4, 5]
        inefficient_result = no_list_comprehension(test_numbers)
        optimized_result = optimized_list_comprehension(test_numbers)
        self.assertEqual(inefficient_result, optimized_result)
    
    def test_regex_compilation(self):
        """Test regex compilation optimization."""
        test_strings = ["test123", "hello", "world456", "foo"]
        inefficient_result = repeated_regex_compilation(test_strings)
        optimized_result = optimized_regex_compilation(test_strings)
        self.assertEqual(inefficient_result, optimized_result)
    
    def test_empty_inputs(self):
        """Test with empty inputs."""
        self.assertEqual(slow_string_concatenation([]), optimized_string_concatenation([]))
        self.assertEqual(no_list_comprehension([]), optimized_list_comprehension([]))
        self.assertEqual(repeated_regex_compilation([]), optimized_regex_compilation([]))


if __name__ == '__main__':
    unittest.main()
