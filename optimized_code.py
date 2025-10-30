"""
Optimized versions of the slow code examples.
These implementations demonstrate best practices and performance improvements.
"""

from typing import List, Iterator
from collections import defaultdict
from functools import lru_cache


def optimized_string_concatenation(items: List[str], iterations: int = 1000) -> str:
    """
    SOLUTION: Use join() method with list
    BENEFIT: O(n) complexity, single memory allocation
    """
    result_parts = []
    for _ in range(iterations):
        for item in items:
            result_parts.append(item)
            result_parts.append(",")
    return "".join(result_parts)


def optimized_list_search(data: List[int], search_values: List[int]) -> List[bool]:
    """
    SOLUTION: Convert list to set for O(1) lookups
    BENEFIT: Much faster membership testing
    """
    data_set = set(data)
    return [value in data_set for value in search_values]


def optimized_list_comprehension(n: int) -> List[int]:
    """
    SOLUTION: Single-pass generator expression
    BENEFIT: No intermediate lists, less memory, single iteration
    """
    return [x ** 2 for x in range(0, n, 2) if x ** 2 > 100]


def optimized_file_reading(filename: str) -> Iterator[str]:
    """
    SOLUTION: Use generator to process line by line
    BENEFIT: Memory efficient for large files
    """
    with open(filename, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                yield stripped.upper()


def optimized_dictionary_operations(items: List[tuple]) -> dict:
    """
    SOLUTION: Use defaultdict or dict.get() with default
    BENEFIT: Single lookup per operation
    """
    result = defaultdict(int)
    for key, value in items:
        result[key] += value
    return dict(result)


def optimized_nested_loops(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """
    SOLUTION: Use numpy for matrix operations (when available)
    FALLBACK: Better cache locality with transposed access
    BENEFIT: Vectorized operations are much faster
    """
    try:
        import numpy as np
        m1 = np.array(matrix1)
        m2 = np.array(matrix2)
        result = np.matmul(m1, m2)
        return result.tolist()
    except ImportError:
        # Fallback: optimize cache locality
        n = len(matrix1)
        m = len(matrix2[0])
        p = len(matrix2)
        
        # Transpose matrix2 for better cache performance
        matrix2_t = [[matrix2[j][i] for j in range(p)] for i in range(m)]
        
        result = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                result[i][j] = sum(matrix1[i][k] * matrix2_t[j][k] for k in range(p))
        
        return result


def optimized_data_filtering(data: List[dict], threshold: int) -> List[dict]:
    """
    SOLUTION: Single-pass filter and efficient sort
    BENEFIT: No redundant copies, O(n log n) sort instead of O(n²)
    """
    return sorted(
        (item for item in data if item.get('value', 0) > threshold),
        key=lambda x: x.get('value', 0)
    )


@lru_cache(maxsize=None)
def optimized_recursive_fibonacci(n: int) -> int:
    """
    SOLUTION: Memoization with lru_cache
    BENEFIT: O(n) time complexity, eliminates redundant calculations
    """
    if n <= 1:
        return n
    return optimized_recursive_fibonacci(n - 1) + optimized_recursive_fibonacci(n - 2)


def optimized_fibonacci_iterative(n: int) -> int:
    """
    ALTERNATIVE SOLUTION: Iterative approach
    BENEFIT: O(n) time, O(1) space, no recursion overhead
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def optimized_duplicate_removal(items: List[int]) -> List[int]:
    """
    SOLUTION: Use set or dict.fromkeys() to preserve order
    BENEFIT: O(n) time complexity
    """
    return list(dict.fromkeys(items))


def optimized_sum_calculation(numbers: List[int]) -> int:
    """
    SOLUTION: Use built-in sum() function
    BENEFIT: Optimized C implementation, faster than Python loop
    """
    return sum(numbers)


# Additional optimization: batch processing example
def optimized_batch_processing(data: List[int], batch_size: int = 1000) -> List[int]:
    """
    SOLUTION: Process data in batches
    BENEFIT: Better cache utilization and memory management
    """
    results = []
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        # Process batch
        processed = [x * 2 for x in batch if x > 0]
        results.extend(processed)
    return results


if __name__ == "__main__":
    print("Optimized code examples loaded. Use benchmark.py to compare performance.")
    
    # Quick test
    test_items = ["item1", "item2", "item3"]
    result = optimized_string_concatenation(test_items, 10)
    print(f"String concatenation result length: {len(result)}")
    
    test_data = list(range(1000))
    searches = [100, 500, 999]
    results = optimized_list_search(test_data, searches)
    print(f"List search results: {results}")
    
    # Test memoized fibonacci
    print(f"Fibonacci(30) = {optimized_recursive_fibonacci(30)}")
