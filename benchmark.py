"""
Performance benchmark comparing inefficient vs optimized code.
"""
import time
import sys
from inefficient_code import (
    slow_string_concatenation,
    inefficient_list_search,
    repeated_expensive_calls,
    nested_loop_inefficiency,
    unnecessary_list_copies,
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
    optimized_global_lookup,
    optimized_dict_iteration,
    optimized_list_comprehension,
    optimized_regex_compilation
)


def benchmark_comparison(name, inefficient_func, optimized_func, test_data, iterations=100):
    """Compare performance of inefficient vs optimized implementations."""
    print(f"\n{'='*60}")
    print(f"Benchmark: {name}")
    print(f"{'='*60}")
    
    # Benchmark inefficient version
    start = time.time()
    for _ in range(iterations):
        if isinstance(test_data, tuple):
            inefficient_func(*test_data)
        else:
            inefficient_func(test_data)
    inefficient_time = time.time() - start
    
    # Benchmark optimized version
    start = time.time()
    for _ in range(iterations):
        if isinstance(test_data, tuple):
            optimized_func(*test_data)
        else:
            optimized_func(test_data)
    optimized_time = time.time() - start
    
    # Calculate improvement
    if optimized_time > 0:
        speedup = inefficient_time / optimized_time
    else:
        # Handle edge case where optimized time is effectively zero
        speedup = 1000.0  # Use a large finite number
    
    improvement_pct = ((inefficient_time - optimized_time) / inefficient_time * 100) if inefficient_time > 0 else 0
    
    print(f"Inefficient: {inefficient_time:.4f}s")
    print(f"Optimized:   {optimized_time:.4f}s")
    print(f"Speedup:     {speedup:.2f}x faster")
    print(f"Improvement: {improvement_pct:.1f}%")
    
    return {
        'name': name,
        'inefficient_time': inefficient_time,
        'optimized_time': optimized_time,
        'speedup': speedup,
        'improvement_pct': improvement_pct
    }


def main():
    """Run all benchmarks."""
    print("Performance Optimization Benchmarks")
    print("=" * 60)
    
    results = []
    
    # 1. String concatenation
    sample_list = list(range(1000))
    results.append(benchmark_comparison(
        "String Concatenation",
        slow_string_concatenation,
        optimized_string_concatenation,
        sample_list,
        iterations=100
    ))
    
    # 2. List search
    large_list = list(range(10000))
    results.append(benchmark_comparison(
        "List Search",
        inefficient_list_search,
        optimized_list_search,
        (large_list, 9999),
        iterations=500
    ))
    
    # 3. Repeated expensive calls
    results.append(benchmark_comparison(
        "Repeated Expensive Calculations",
        repeated_expensive_calls,
        optimized_expensive_calls,
        100,
        iterations=50
    ))
    
    # 4. Nested loops
    list1 = list(range(500))
    list2 = list(range(400, 900))
    results.append(benchmark_comparison(
        "Nested Loops (Finding Matches)",
        nested_loop_inefficiency,
        optimized_nested_loops,
        (list1, list2),
        iterations=50
    ))
    
    # 5. Unnecessary copies
    large_data = list(range(10000))
    results.append(benchmark_comparison(
        "List Copies",
        unnecessary_list_copies,
        optimized_list_copies,
        large_data,
        iterations=1000
    ))
    
    # 6. Global lookups in loop
    items = list(range(1000))
    results.append(benchmark_comparison(
        "Global Lookups in Loop",
        global_lookup_in_loop,
        optimized_global_lookup,
        items,
        iterations=500
    ))
    
    # 7. Dictionary iteration
    test_dict = {f"key_{i}": i for i in range(1000)}
    results.append(benchmark_comparison(
        "Dictionary Iteration",
        inefficient_dict_iteration,
        optimized_dict_iteration,
        test_dict,
        iterations=1000
    ))
    
    # 8. List comprehension vs append
    numbers = list(range(1000))
    results.append(benchmark_comparison(
        "List Building (append vs comprehension)",
        no_list_comprehension,
        optimized_list_comprehension,
        numbers,
        iterations=500
    ))
    
    # 9. Regex compilation
    strings = ["test123", "hello", "world456", "foo", "bar789"] * 100
    results.append(benchmark_comparison(
        "Regex Compilation",
        repeated_regex_compilation,
        optimized_regex_compilation,
        strings,
        iterations=100
    ))
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    
    total_inefficient = sum(r['inefficient_time'] for r in results)
    total_optimized = sum(r['optimized_time'] for r in results)
    avg_speedup = sum(r['speedup'] for r in results) / len(results)
    
    print(f"\nTotal time (inefficient): {total_inefficient:.4f}s")
    print(f"Total time (optimized):   {total_optimized:.4f}s")
    print(f"Overall speedup:          {total_inefficient/total_optimized:.2f}x")
    print(f"Average speedup:          {avg_speedup:.2f}x")
    
    print(f"\nTop 3 Improvements:")
    sorted_results = sorted(results, key=lambda x: x['speedup'], reverse=True)
    for i, result in enumerate(sorted_results[:3], 1):
        print(f"{i}. {result['name']}: {result['speedup']:.2f}x faster")


if __name__ == "__main__":
    main()
