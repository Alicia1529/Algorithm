deque

```python
from collections import deque
# Each bucket = (second_bucket, count)
# Slide the window as time advances




import bisect
lo = bisect.bisect_left(timestamps, start)
hi = bisect.bisect_right(timestamps, end)

def bisect_left(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:   # < : stop AT target, go left
            lo = mid + 1
        else:
            hi = mid
    return lo

def bisect_right(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:  # <=: go PAST target, go right
            lo = mid + 1
        else:
            hi = mid
    return lo
    


from threading import Lock
self._lock = Lock()
with self._lock:
    self._get_ts.append(time.time())
    return self._store.get(key)
```


heap / priority queue (`heapq` — min-heap on a plain list)

```python
import heapq

# --- build / push / pop ---
h = [5, 1, 3, 8, 2]
heapq.heapify(h)            # build in-place           O(n)   ← NOT O(n log n)
heapq.heappush(h, x)       # insert                   O(log n)
smallest = heapq.heappop(h)   # remove + return min   O(log n)
peek = h[0]                # min without removing     O(1)

heapq.heappushpop(h, x)    # push x, then pop min      O(log n)  (push first)
heapq.heapreplace(h, x)    # pop min, then push x      O(log n)  (pop first)

heapq.nsmallest(k, iterable)  # k smallest             O(n log k)
heapq.nlargest(k, iterable)   # k largest              O(n log k)

len(h)                     # size                     O(1)
# emptiness: `if not h:`                                O(1)
```

```python
# --- ITERATION GOTCHA ---
# A heap is NOT sorted. Iterating the list gives heap order, only h[0] is the min.
for x in h:                # O(n), arbitrary order — usually NOT what you want
    ...

# Iterate in priority (sorted) order:
tmp = h[:]                 # O(n) copy (non-destructive)
ordered = [heapq.heappop(tmp) for _ in range(len(tmp))]   # O(n log n)

while h:                   # destructive drain, smallest-first   O(n log n)
    x = heapq.heappop(h)

# If you don't need the heap structure, just: sorted(h)        O(n log n)
```

```python
# --- max-heap: Python only has a min-heap, so negate ---
heapq.heappush(h, -x)              # pop gives -max → negate back
heapq.heappush(h, (-priority, item))   # negate the key, keep payload

# --- tie-breaking: push (key, tiebreak, item) so unorderable items never compare ---
import itertools
counter = itertools.count()
heapq.heappush(h, (priority, next(counter), item))   # counter breaks key ties
```

build-from-list complexity: `heapify` is **O(n)** (bottom-up sift-down; most nodes are leaves
that barely move). Building via n separate `heappush` calls is **O(n log n)** — prefer
`heapify` when you have all elements up front.





