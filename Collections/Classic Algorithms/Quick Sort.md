# Quick Sort

Overview
- Divide-and-conquer in-place sort with average O(n log n) time.

Python (in-place Lomuto partition)
```python
import random

def quicksort(a, lo=0, hi=None):
    if hi is None:
        hi = len(a)-1
    if lo < hi:
        p = partition(a, lo, hi)
        quicksort(a, lo, p-1)
        quicksort(a, p+1, hi)

def partition(a, lo, hi):
    pivot_idx = random.randint(lo, hi)
    a[pivot_idx], a[hi] = a[hi], a[pivot_idx]
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i

# Example:
# arr = [3,6,1,8,4]
# quicksort(arr)
# arr -> sorted
```
