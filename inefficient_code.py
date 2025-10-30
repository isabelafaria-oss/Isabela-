"""
Example of inefficient code patterns that need optimization.
This module demonstrates common performance anti-patterns.
"""
import time


def slow_string_concatenation(items):
    """Inefficient: Using + for string concatenation in a loop."""
    result = ""
    for item in items:
        result = result + str(item) + ","
    return result


def inefficient_list_search(data_list, target):
    """Inefficient: Linear search when better data structures exist."""
    found_items = []
    for item in data_list:
        if item == target:
            found_items.append(item)
    return found_items


def repeated_expensive_calls(n):
    """Inefficient: Recalculating the same value multiple times."""
    results = []
    for i in range(n):
        # Expensive calculation repeated in loop
        expensive_value = sum(range(10000))
        results.append(i * expensive_value)
    return results


def nested_loop_inefficiency(list1, list2):
    """Inefficient: Nested loops with O(n²) complexity."""
    matches = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                matches.append(item1)
    return matches


def unnecessary_list_copies(data):
    """Inefficient: Creating unnecessary copies of large lists."""
    copy1 = data[:]
    copy2 = copy1[:]
    copy3 = copy2[:]
    return copy3


def inefficient_file_reading(filename):
    """Inefficient: Reading file line by line without buffering."""
    try:
        lines = []
        with open(filename, 'r') as f:
            line = f.readline()
            while line:
                lines.append(line.strip())
                line = f.readline()
        return lines
    except FileNotFoundError:
        return []


def global_lookup_in_loop(items):
    """Inefficient: Looking up global functions in tight loops."""
    result = []
    for item in items:
        result.append(len(str(item)))
    return result


def inefficient_dict_iteration(data_dict):
    """Inefficient: Checking if key exists, then accessing it."""
    results = []
    for key in data_dict.keys():
        if key in data_dict:
            results.append(data_dict[key])
    return results


def no_list_comprehension(numbers):
    """Inefficient: Using append in loop instead of list comprehension."""
    squares = []
    for num in numbers:
        squares.append(num ** 2)
    return squares


def repeated_regex_compilation(strings):
    """Inefficient: Compiling regex inside loop."""
    import re
    matches = []
    for string in strings:
        pattern = re.compile(r'\d+')
        if pattern.search(string):
            matches.append(string)
    return matches


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
    
    print("Running benchmarks on inefficient code...")
    print(f"String concatenation: {benchmark_function(slow_string_concatenation, sample_list):.4f}s")
    print(f"Nested loops: {benchmark_function(nested_loop_inefficiency, sample_list[:100], sample_list[:100]):.4f}s")
    print(f"Repeated calculations: {benchmark_function(repeated_expensive_calls, 100):.4f}s")
