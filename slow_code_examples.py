"""
Examples of slow/inefficient code patterns.
These examples demonstrate common performance issues.
"""

import time
from typing import List


def inefficient_string_concatenation(items: List[str], iterations: int = 1000) -> str:
    """
    ISSUE: Using + operator in a loop for string concatenation
    PROBLEM: Creates new string object on each iteration (O(n²) complexity)
    """
    result = ""
    for _ in range(iterations):
        for item in items:
            result = result + item + ","
    return result


def inefficient_list_search(data: List[int], search_values: List[int]) -> List[bool]:
    """
    ISSUE: Using list for membership testing
    PROBLEM: O(n) lookup time for each search
    """
    results = []
    for value in search_values:
        results.append(value in data)
    return results


def inefficient_list_comprehension(n: int) -> List[int]:
    """
    ISSUE: Multiple passes over data
    PROBLEM: Separate filter and map operations create intermediate lists
    """
    numbers = list(range(n))
    # First pass: filter
    filtered = [x for x in numbers if x % 2 == 0]
    # Second pass: map
    squared = [x ** 2 for x in filtered]
    # Third pass: filter again
    result = [x for x in squared if x > 100]
    return result


def inefficient_file_reading(filename: str) -> List[str]:
    """
    ISSUE: Reading entire file into memory
    PROBLEM: Memory inefficient for large files
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    processed = []
    for line in lines:
        if line.strip():
            processed.append(line.upper())
    return processed


def inefficient_dictionary_operations(items: List[tuple]) -> dict:
    """
    ISSUE: Repeated key lookups and checks
    PROBLEM: Multiple dictionary accesses for same key
    """
    result = {}
    for key, value in items:
        if key in result:
            result[key] = result[key] + value
        else:
            result[key] = value
    return result


def inefficient_nested_loops(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """
    ISSUE: Naive matrix multiplication
    PROBLEM: Poor cache locality and no vectorization
    """
    n = len(matrix1)
    m = len(matrix2[0])
    p = len(matrix2)
    
    result = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result


def inefficient_data_filtering(data: List[dict], threshold: int) -> List[dict]:
    """
    ISSUE: Creating temporary lists and multiple iterations
    PROBLEM: Inefficient memory usage and redundant operations
    """
    temp_list = []
    for item in data:
        temp_list.append(item)
    
    filtered = []
    for item in temp_list:
        if item.get('value', 0) > threshold:
            filtered.append(item)
    
    sorted_data = []
    while filtered:
        min_item = min(filtered, key=lambda x: x.get('value', 0))
        filtered.remove(min_item)
        sorted_data.append(min_item)
    
    return sorted_data


def inefficient_recursive_fibonacci(n: int) -> int:
    """
    ISSUE: Naive recursion without memoization
    PROBLEM: Exponential time complexity O(2^n)
    """
    if n <= 1:
        return n
    return inefficient_recursive_fibonacci(n - 1) + inefficient_recursive_fibonacci(n - 2)


def inefficient_duplicate_removal(items: List[int]) -> List[int]:
    """
    ISSUE: Using nested loop for duplicate detection
    PROBLEM: O(n²) time complexity
    """
    result = []
    for item in items:
        is_duplicate = False
        for existing in result:
            if existing == item:
                is_duplicate = True
                break
        if not is_duplicate:
            result.append(item)
    return result


def inefficient_sum_calculation(numbers: List[int]) -> int:
    """
    ISSUE: Manual iteration instead of built-in functions
    PROBLEM: Slower than optimized built-ins
    """
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total


if __name__ == "__main__":
    # Simple demonstrations
    print("Slow code examples loaded. Use benchmark.py to measure performance.")
    
    # Quick test
    test_items = ["item1", "item2", "item3"]
    result = inefficient_string_concatenation(test_items, 10)
    print(f"String concatenation result length: {len(result)}")
    
    test_data = list(range(1000))
    searches = [100, 500, 999]
    results = inefficient_list_search(test_data, searches)
    print(f"List search results: {results}")
