"""
Optimized version of the inefficient code patterns.
This module demonstrates performance best practices.
"""
import time
import re


def optimized_string_concatenation(items):
    """Optimized: Using join() for efficient string building."""
    if not items:
        return ""
    return ",".join(str(item) for item in items) + ","


def optimized_list_search(data_list, target):
    """Optimized: Using set for O(1) lookup instead of O(n)."""
    data_set = set(data_list)
    return [target] if target in data_set else []


def optimized_expensive_calls(n):
    """Optimized: Calculate once and reuse the value."""
    expensive_value = sum(range(10000))
    results = [i * expensive_value for i in range(n)]
    return results


def optimized_nested_loops(list1, list2):
    """Optimized: Using set intersection for O(n+m) instead of O(n²)."""
    return list(set(list1) & set(list2))


def optimized_list_copies(data):
    """Optimized: Return reference when modification not needed."""
    # If you truly need a copy, one is sufficient
    return data


def optimized_file_reading(filename):
    """Optimized: Read all lines at once with readlines()."""
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []


def optimized_global_lookup(items):
    """Optimized: Cache global lookups outside the loop."""
    str_func = str
    len_func = len
    return [len_func(str_func(item)) for item in items]


def optimized_dict_iteration(data_dict):
    """Optimized: Direct iteration over values or items."""
    return list(data_dict.values())


def optimized_list_comprehension(numbers):
    """Optimized: Using list comprehension for better performance."""
    return [num ** 2 for num in numbers]


def optimized_regex_compilation(strings):
    """Optimized: Compile regex once before the loop."""
    pattern = re.compile(r'\d+')
    return [string for string in strings if pattern.search(string)]


# Benchmark functions
def benchmark_function(func, *args, iterations=1000):
    """Simple benchmark helper."""
    start = time.time()
    for _ in range(iterations):
        func(*args)
    end = time.time()
    return end - start


if __name__ == "__main__":
    # Test with sample data
    sample_list = list(range(1000))
    sample_strings = ["test123", "hello", "world456"] * 100
    
    print("Running benchmarks on optimized code...")
    print(f"String concatenation: {benchmark_function(optimized_string_concatenation, sample_list):.4f}s")
    print(f"Set intersection: {benchmark_function(optimized_nested_loops, sample_list[:100], sample_list[:100]):.4f}s")
    print(f"Cached calculations: {benchmark_function(optimized_expensive_calls, 100):.4f}s")
