# Performance Optimization Guide

This repository demonstrates common performance issues in Python code and their optimized solutions.

## 📚 Contents

- **slow_code_examples.py** - Examples of inefficient code patterns
- **optimized_code.py** - Optimized implementations
- **benchmark.py** - Performance comparison suite
- **tests/** - Unit tests for both implementations

## 🚀 Quick Start

### Run Benchmarks

```bash
python benchmark.py
```

This will compare the performance of slow vs. optimized implementations across various scenarios.

### Run Tests

```bash
python -m pytest tests/ -v
```

## 📊 Common Performance Issues Covered

### 1. String Concatenation
**Problem:** Using `+` operator in loops creates new string objects repeatedly (O(n²))
**Solution:** Use `str.join()` for O(n) complexity

```python
# Slow ❌
result = ""
for item in items:
    result = result + item + ","

# Fast ✅
result = ",".join(items) + ","
```

### 2. List Membership Testing
**Problem:** Using `in` operator on lists requires O(n) time per lookup
**Solution:** Convert to `set` for O(1) lookups

```python
# Slow ❌
for value in search_values:
    if value in large_list:  # O(n) each time
        ...

# Fast ✅
data_set = set(large_list)  # O(n) once
for value in search_values:
    if value in data_set:  # O(1) each time
        ...
```

### 3. Multiple Passes Over Data
**Problem:** Separate filter/map operations create intermediate lists
**Solution:** Single-pass comprehension or generator expression

```python
# Slow ❌
filtered = [x for x in range(n) if x % 2 == 0]
squared = [x ** 2 for x in filtered]
result = [x for x in squared if x > 100]

# Fast ✅
result = [x ** 2 for x in range(0, n, 2) if x ** 2 > 100]
```

### 4. File Reading
**Problem:** Loading entire file into memory
**Solution:** Use generators to process line by line

```python
# Slow ❌
with open(filename) as f:
    lines = f.readlines()  # Entire file in memory
    for line in lines:
        process(line)

# Fast ✅
with open(filename) as f:
    for line in f:  # One line at a time
        process(line)
```

### 5. Dictionary Operations
**Problem:** Repeated key lookups and checks
**Solution:** Use `defaultdict` or `dict.get()` with defaults

```python
# Slow ❌
for key, value in items:
    if key in result:
        result[key] = result[key] + value
    else:
        result[key] = value

# Fast ✅
from collections import defaultdict
result = defaultdict(int)
for key, value in items:
    result[key] += value
```

### 6. Naive Recursion
**Problem:** Exponential time complexity due to redundant calculations
**Solution:** Use memoization or convert to iteration

```python
# Slow ❌ - O(2^n)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Fast ✅ - O(n) with memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Fastest ✅ - O(n) iterative
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### 7. Duplicate Removal
**Problem:** Using nested loops for duplicate detection (O(n²))
**Solution:** Use set or dict for O(n) complexity

```python
# Slow ❌
result = []
for item in items:
    if item not in result:  # O(n) check
        result.append(item)

# Fast ✅
result = list(dict.fromkeys(items))  # Preserves order
# or
result = list(set(items))  # Doesn't preserve order but faster
```

### 8. Manual Sum Calculation
**Problem:** Manual iteration is slower than built-in functions
**Solution:** Use optimized built-ins

```python
# Slow ❌
total = 0
for i in range(len(numbers)):
    total = total + numbers[i]

# Fast ✅
total = sum(numbers)
```

### 9. Matrix Operations
**Problem:** Naive nested loops with poor cache locality
**Solution:** Use NumPy for vectorized operations

```python
# Slow ❌
result = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        for k in range(p):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# Fast ✅
import numpy as np
result = np.matmul(matrix1, matrix2)
```

## 🎯 Best Practices

1. **Use Built-in Functions** - They're implemented in C and highly optimized
2. **Choose Right Data Structures** - Sets for membership, deques for queues, etc.
3. **Avoid Premature Optimization** - Profile first, optimize bottlenecks
4. **Generator Expressions** - For large datasets to save memory
5. **List Comprehensions** - Faster than equivalent for loops
6. **Avoid Global Variables** - Local lookups are faster
7. **Cache Expensive Operations** - Use `@lru_cache` or custom caching
8. **Batch Operations** - Process data in chunks for better cache usage

## 📈 Expected Performance Improvements

Based on benchmark results, you can expect:

- **String concatenation**: 10-100x faster with join()
- **List searches**: 50-500x faster with sets
- **Fibonacci(25)**: 1000-10000x faster with memoization
- **Dictionary operations**: 2-5x faster with proper methods
- **File processing**: 50-90% less memory with generators
- **Sum calculations**: 2-5x faster with built-ins

## 🧪 Testing

All implementations include unit tests to ensure correctness:

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_slow_code.py -v

# Run with coverage
python -m pytest tests/ --cov=. --cov-report=html
```

## 🔍 Profiling

To identify performance bottlenecks in your own code:

```python
import cProfile
import pstats

# Profile a function
cProfile.run('your_function()', 'output.stats')

# Analyze results
stats = pstats.Stats('output.stats')
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 functions
```

Or use line_profiler for line-by-line analysis:

```bash
pip install line_profiler
kernprof -l -v your_script.py
```

## 📚 Additional Resources

- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
- [Time Complexity Reference](https://wiki.python.org/moin/TimeComplexity)
- [Profiling Python Code](https://docs.python.org/3/library/profile.html)
- [NumPy Performance Tips](https://numpy.org/doc/stable/user/performance.html)

## 🤝 Contributing

Found more performance anti-patterns? Feel free to contribute!

1. Add the slow example to `slow_code_examples.py`
2. Add the optimized version to `optimized_code.py`
3. Add benchmark in `benchmark.py`
4. Add tests in `tests/`
5. Update this README with the pattern

## 📄 License

This project is for educational purposes.
