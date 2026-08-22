# Quick Select

Overview
- Select the k-th smallest element in expected O(n) time (partition-based).

Python (in-place)
```python
import random

def quickselect(a, k, lo=0, hi=None):
    if hi is None:
        hi = len(a)-1
    while True:
        if lo == hi:
            return a[lo]
        pivot_idx = random.randint(lo, hi)
        a[pivot_idx], a[hi] = a[hi], a[pivot_idx]
        p = partition(a, lo, hi)
        if k == p:
            return a[p]
        elif k < p:
            hi = p-1
        else:
            lo = p+1

def partition(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i

# Example: quickselect([3,2,1,5,4], 2) -> 3 (0-based k)
```
