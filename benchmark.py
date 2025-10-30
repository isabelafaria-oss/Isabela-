"""
Performance benchmarking suite.
Compares slow vs optimized implementations.
"""

import time
import sys
from typing import Callable, Any
import tracemalloc

# Import slow and optimized versions
import slow_code_examples as slow
import optimized_code as fast


def measure_performance(func: Callable, *args, **kwargs) -> dict:
    """
    Measure execution time and memory usage of a function.
    
    Returns:
        dict with 'time' (seconds) and 'memory' (MB) keys
    """
    # Measure memory
    tracemalloc.start()
    
    # Measure time
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    
    # Get memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return {
        'time': end_time - start_time,
        'memory': peak / (1024 * 1024),  # Convert to MB
        'result': result
    }


def format_improvement(slow_val: float, fast_val: float) -> str:
    """Format the improvement factor with color coding."""
    if fast_val == 0:
        return "∞x faster"
    improvement = slow_val / fast_val
    if improvement > 1:
        return f"{improvement:.2f}x faster"
    else:
        return f"{1/improvement:.2f}x slower"


def print_benchmark_header(test_name: str):
    """Print a formatted header for benchmark section."""
    print("\n" + "=" * 80)
    print(f"  {test_name}")
    print("=" * 80)


def run_benchmark(test_name: str, slow_func: Callable, fast_func: Callable, 
                  *args, **kwargs):
    """
    Run benchmark comparing slow and optimized implementations.
    """
    print_benchmark_header(test_name)
    
    print("\nRunning slow version...")
    slow_metrics = measure_performance(slow_func, *args, **kwargs)
    
    print("Running optimized version...")
    fast_metrics = measure_performance(fast_func, *args, **kwargs)
    
    # Print results
    print(f"\n{'Metric':<20} {'Slow':<20} {'Optimized':<20} {'Improvement':<20}")
    print("-" * 80)
    print(f"{'Execution Time':<20} {slow_metrics['time']:.6f}s {fast_metrics['time']:.6f}s {format_improvement(slow_metrics['time'], fast_metrics['time']):<20}")
    print(f"{'Memory Usage':<20} {slow_metrics['memory']:.4f} MB {fast_metrics['memory']:.4f} MB {format_improvement(slow_metrics['memory'], fast_metrics['memory']):<20}")


def main():
    """Run all benchmarks."""
    print("=" * 80)
    print("  PERFORMANCE BENCHMARK SUITE")
    print("  Comparing Slow vs Optimized Code")
    print("=" * 80)
    
    # 1. String Concatenation
    test_items = ["item"] * 100
    run_benchmark(
        "1. String Concatenation (1000 iterations)",
        slow.inefficient_string_concatenation,
        fast.optimized_string_concatenation,
        test_items, 1000
    )
    
    # 2. List Search
    large_list = list(range(10000))
    search_items = list(range(0, 10000, 100))
    run_benchmark(
        "2. List Membership Testing (10k items, 100 searches)",
        slow.inefficient_list_search,
        fast.optimized_list_search,
        large_list, search_items
    )
    
    # 3. List Comprehension
    run_benchmark(
        "3. List Filtering and Transformation (10k items)",
        slow.inefficient_list_comprehension,
        fast.optimized_list_comprehension,
        10000
    )
    
    # 4. Dictionary Operations
    items = [(f"key{i % 100}", i) for i in range(1000)]
    run_benchmark(
        "4. Dictionary Aggregation (1k items)",
        slow.inefficient_dictionary_operations,
        fast.optimized_dictionary_operations,
        items
    )
    
    # 5. Duplicate Removal
    duplicated_list = [i % 100 for i in range(1000)]
    run_benchmark(
        "5. Duplicate Removal (1k items with duplicates)",
        slow.inefficient_duplicate_removal,
        fast.optimized_duplicate_removal,
        duplicated_list
    )
    
    # 6. Sum Calculation
    numbers = list(range(10000))
    run_benchmark(
        "6. Sum Calculation (10k numbers)",
        slow.inefficient_sum_calculation,
        fast.optimized_sum_calculation,
        numbers
    )
    
    # 7. Fibonacci (smaller number due to exponential complexity)
    print_benchmark_header("7. Fibonacci Calculation (n=25)")
    print("\nRunning slow recursive version (this may take a while)...")
    slow_fib = measure_performance(slow.inefficient_recursive_fibonacci, 25)
    
    print("Running optimized memoized version...")
    fast_fib_memo = measure_performance(fast.optimized_recursive_fibonacci, 25)
    
    print("Running optimized iterative version...")
    fast_fib_iter = measure_performance(fast.optimized_fibonacci_iterative, 25)
    
    print(f"\n{'Version':<30} {'Time':<20} {'Improvement':<20}")
    print("-" * 70)
    print(f"{'Slow (naive recursion)':<30} {slow_fib['time']:.6f}s {'baseline':<20}")
    print(f"{'Optimized (memoization)':<30} {fast_fib_memo['time']:.6f}s {format_improvement(slow_fib['time'], fast_fib_memo['time']):<20}")
    print(f"{'Optimized (iterative)':<30} {fast_fib_iter['time']:.6f}s {format_improvement(slow_fib['time'], fast_fib_iter['time']):<20}")
    
    # 8. Matrix Multiplication (small matrices)
    matrix_size = 50
    matrix1 = [[i + j for j in range(matrix_size)] for i in range(matrix_size)]
    matrix2 = [[i * j for j in range(matrix_size)] for i in range(matrix_size)]
    run_benchmark(
        f"8. Matrix Multiplication ({matrix_size}x{matrix_size})",
        slow.inefficient_nested_loops,
        fast.optimized_nested_loops,
        matrix1, matrix2
    )
    
    # 9. Data Filtering and Sorting
    data = [{'id': i, 'value': i % 200} for i in range(1000)]
    run_benchmark(
        "9. Data Filtering and Sorting (1k items, threshold=100)",
        slow.inefficient_data_filtering,
        fast.optimized_data_filtering,
        data, 100
    )
    
    # Final summary
    print("\n" + "=" * 80)
    print("  BENCHMARK COMPLETE")
    print("=" * 80)
    print("\nKey Takeaways:")
    print("  • Use built-in functions (sum, sorted, etc.) - they're optimized")
    print("  • Convert lists to sets for frequent membership tests")
    print("  • Use join() for string concatenation instead of +=")
    print("  • Prefer dict methods that avoid redundant lookups")
    print("  • Use memoization or iteration instead of naive recursion")
    print("  • Process files line-by-line with generators for large files")
    print("  • Use single-pass operations instead of multiple iterations")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
