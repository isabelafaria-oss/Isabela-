# Code Optimization Guide

This repository demonstrates common performance anti-patterns and their optimized solutions.

## Overview

This project identifies and fixes slow or inefficient code patterns commonly found in Python applications. Each optimization is benchmarked to demonstrate the performance improvement.

## Performance Issues Identified

### 1. String Concatenation in Loops
**Problem:** Using `+` operator for string concatenation in loops creates a new string object each iteration.

**Inefficient:**
```python
result = ""
for item in items:
    result = result + str(item) + ","
```

**Optimized:**
```python
return ",".join(str(item) for item in items)
```

**Impact:** ~10-100x faster depending on data size. String concatenation with `+` is O(n²) while `join()` is O(n).

---

### 2. Linear Search Instead of Set/Dict Lookup
**Problem:** Using `in` operator with lists requires O(n) linear search.

**Inefficient:**
```python
found_items = []
for item in data_list:
    if item == target:
        found_items.append(item)
```

**Optimized:**
```python
data_set = set(data_list)
return [target] if target in data_set else []
```

**Impact:** ~100-1000x faster for large lists. Set lookup is O(1) vs O(n) for lists.

---

### 3. Repeated Expensive Calculations
**Problem:** Recalculating the same value in each loop iteration.

**Inefficient:**
```python
results = []
for i in range(n):
    expensive_value = sum(range(10000))  # Recalculated each time!
    results.append(i * expensive_value)
```

**Optimized:**
```python
expensive_value = sum(range(10000))  # Calculate once
results = [i * expensive_value for i in range(n)]
```

**Impact:** ~10-50x faster. Eliminates redundant computation.

---

### 4. Nested Loops (O(n²) Complexity)
**Problem:** Using nested loops to find matches between two lists.

**Inefficient:**
```python
matches = []
for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            matches.append(item1)
```

**Optimized:**
```python
return list(set(list1) & set(list2))
```

**Impact:** ~100-10000x faster. Reduces O(n²) to O(n+m) complexity.

---

### 5. Unnecessary Data Copies
**Problem:** Creating multiple unnecessary copies of large data structures.

**Inefficient:**
```python
copy1 = data[:]
copy2 = copy1[:]
copy3 = copy2[:]
return copy3
```

**Optimized:**
```python
return data  # Return reference if no modification needed
```

**Impact:** ~5-10x faster and uses much less memory.

---

### 6. Global Lookups in Tight Loops
**Problem:** Python looks up built-in functions in global scope on each iteration.

**Inefficient:**
```python
result = []
for item in items:
    result.append(len(str(item)))  # Global lookups every iteration
```

**Optimized:**
```python
str_func = str  # Cache lookups
len_func = len
return [len_func(str_func(item)) for item in items]
```

**Impact:** ~2-3x faster for tight loops with many iterations.

---

### 7. Inefficient Dictionary Iteration
**Problem:** Redundantly checking if key exists when iterating.

**Inefficient:**
```python
results = []
for key in data_dict.keys():
    if key in data_dict:  # Redundant check
        results.append(data_dict[key])
```

**Optimized:**
```python
return list(data_dict.values())  # Direct value access
```

**Impact:** ~2-5x faster. Eliminates redundant operations.

---

### 8. Append in Loop vs List Comprehension
**Problem:** Using append() method in a loop is slower than list comprehension.

**Inefficient:**
```python
squares = []
for num in numbers:
    squares.append(num ** 2)
```

**Optimized:**
```python
return [num ** 2 for num in numbers]
```

**Impact:** ~1.5-2x faster. List comprehensions are optimized in CPython.

---

### 9. Repeated Regex Compilation
**Problem:** Compiling the same regex pattern inside a loop.

**Inefficient:**
```python
import re
matches = []
for string in strings:
    pattern = re.compile(r'\d+')  # Compiled every iteration!
    if pattern.search(string):
        matches.append(string)
```

**Optimized:**
```python
import re
pattern = re.compile(r'\d+')  # Compile once
return [string for string in strings if pattern.search(string)]
```

**Impact:** ~5-10x faster. Regex compilation is expensive.

---

## Running the Benchmarks

To see the performance improvements in action:

```bash
python benchmark.py
```

This will run comprehensive benchmarks comparing inefficient vs optimized implementations and display:
- Execution time for each approach
- Speedup factor
- Percentage improvement
- Overall summary statistics

## Key Takeaways

1. **Use appropriate data structures**: Sets/dicts for lookups, lists for sequential access
2. **Avoid premature optimization**: Profile first, optimize bottlenecks
3. **Cache expensive operations**: Don't repeat expensive calculations
4. **Use built-in functions**: Python's built-ins are optimized in C
5. **Prefer list comprehensions**: More Pythonic and faster than loops
6. **Compile regex once**: Store compiled patterns for reuse
7. **Reduce algorithmic complexity**: O(n) is better than O(n²)
8. **Minimize memory allocations**: Avoid unnecessary copies
9. **Profile your code**: Use tools like cProfile, line_profiler
10. **Benchmark changes**: Always measure to confirm improvements

## Tools for Profiling

- `cProfile`: Built-in profiler for function-level analysis
- `line_profiler`: Line-by-line profiling
- `memory_profiler`: Memory usage tracking
- `timeit`: Accurate timing of small code snippets
- `py-spy`: Sampling profiler with minimal overhead

## References

- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
- [Time Complexity of Python Operations](https://wiki.python.org/moin/TimeComplexity)
- [Python Optimization Guide](https://docs.python.org/3/howto/perf_tuning.html)
