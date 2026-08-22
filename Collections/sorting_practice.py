"""
Sorting Algorithms Practice Runner
Run: python sorting_practice.py
"""

import random
import time


# ── Algorithms ────────────────────────────────────────────────────────────────


def bubble_sort(arr):
    arr = arr[:]
    # TIME:  Two nested loops.
    #        Outer runs n times; inner runs (n-1) + (n-2) + ... + 1 = n(n-1)/2 times → O(n²).
    #        Best case: array already sorted — can add an early-exit flag to get O(n),
    #        but this implementation always does all passes → O(n²) best too.
    # SPACE: Sorting is done in-place with only a temp variable for swaps → O(1).
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    # TIME:  Two nested loops.
    #        For each of the n positions, we scan the remaining unsorted portion:
    #        (n-1) + (n-2) + ... + 1 = n(n-1)/2 comparisons → O(n²) always.
    #        Unlike bubble sort, no early exit is possible — must scan to find the minimum.
    # SPACE: In-place swaps only → O(1).
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    # TIME:  Outer loop runs n-1 times. Inner while loop shifts elements left.
    #        Worst case (reverse sorted): element i must shift past all i elements → 1+2+...+(n-1) = O(n²).
    #        Best case (already sorted): inner while never executes → O(n).
    #        This makes it ideal for nearly-sorted data or small arrays.
    # SPACE: In-place; only `key` and `j` are extra variables → O(1).
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    # TIME:  Recurrence: T(n) = 2T(n/2) + O(n).
    #        The array is halved at each level → log n levels.
    #        Each level does O(n) work to merge → O(n log n) total. Same in all cases.
    # SPACE: Each merge call allocates a new `result` list.
    #        At any point, the call stack is log n deep, and each level holds O(n)
    #        elements across all merge buffers at that level → O(n) total auxiliary space.
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    # TIME:  Recurrence depends on pivot quality.
    #        Average (random pivot): T(n) = 2T(n/2) + O(n) → O(n log n).
    #        Worst case (pivot always min/max, e.g. sorted input with last-element pivot):
    #          T(n) = T(n-1) + O(n) → O(n²).
    #        partition() does one linear scan of the subarray → O(n) per call.
    # SPACE: No extra array; in-place swaps. But recursion depth matters.
    #        Average: O(log n) call stack. Worst: O(n) call stack (skewed splits).
    arr = arr[:]

    def _quick(lo, hi):
        if lo < hi:
            p = partition(lo, hi)
            _quick(lo, p - 1)
            _quick(p + 1, hi)

    def partition(lo, hi):
        pivot = arr[hi]
        i = lo - 1
        for j in range(lo, hi):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
        return i + 1

    _quick(0, len(arr) - 1)
    return arr


def heap_sort(arr):
    # TIME:  Two phases:
    #        1. Build max-heap: n/2 heapify calls, each O(log n) → O(n).
    #           (Tighter analysis gives O(n) because lower nodes do less work.)
    #        2. Extract max n-1 times: each swap + heapify is O(log n) → O(n log n).
    #        Total: O(n log n) in all cases — no best/worst difference.
    # SPACE: In-place; heapify is recursive but bounded by heap height = log n → O(log n).
    #        Can be made O(1) with an iterative heapify.
    arr = arr[:]
    n = len(arr)

    def heapify(size, i):
        largest, l, r = i, 2*i+1, 2*i+2
        if l < size and arr[l] > arr[largest]:
            largest = l
        if r < size and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
    return arr


def counting_sort(arr):
    # TIME:  Three passes:
    #        1. Find max → O(n).
    #        2. Tally counts → O(n).
    #        3. Reconstruct output by iterating count array of size k → O(n + k).
    #        Total: O(n + k), where k = max value. Efficient when k = O(n).
    # SPACE: count array of size k+1, plus output array of size n → O(n + k).
    #        Not in-place; trades memory for linear time.
    if not arr:
        return arr[:]
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for x in arr:
        count[x] += 1
    result = []
    for val, freq in enumerate(count):
        result.extend([val] * freq)
    return result


def bucket_sort(arr):
    # Works for floats in [0, 1).
    # TIME:  Distribute n elements into n buckets → O(n).
    #        Sort each bucket with sorted() (Timsort): if input is uniform,
    #        each bucket has O(1) elements on average → O(n) total sorting.
    #        Overall average: O(n + k) where k = number of buckets (here k = n) → O(n).
    #        Worst case: all elements fall into one bucket → O(n²) (one bucket, full sort).
    # SPACE: n buckets each holding portions of the input → O(n + k) = O(n).
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for x in arr:
        buckets[int(x * n)].append(x)
    result = []
    for b in buckets:
        result.extend(sorted(b))
    return result


# ── Runner ────────────────────────────────────────────────────────────────────

# (name, fn, time_best, time_avg, time_worst, space, stable)
ALGORITHMS = [
    ("Bubble Sort",    bubble_sort,    "O(n)",       "O(n²)",      "O(n²)",      "O(1)",      True),
    ("Selection Sort", selection_sort, "O(n²)",      "O(n²)",      "O(n²)",      "O(1)",      False),
    ("Insertion Sort", insertion_sort, "O(n)",       "O(n²)",      "O(n²)",      "O(1)",      True),
    ("Merge Sort",     merge_sort,     "O(n log n)", "O(n log n)", "O(n log n)", "O(n)",      True),
    ("Quick Sort",     quick_sort,     "O(n log n)", "O(n log n)", "O(n²)",      "O(log n)",  False),
    ("Heap Sort",      heap_sort,      "O(n log n)", "O(n log n)", "O(n log n)", "O(1)",      False),
    ("Counting Sort",  counting_sort,  "O(n+k)",     "O(n+k)",     "O(n+k)",     "O(k)",      True),
    ("Bucket Sort",    bucket_sort,    "O(n+k)",     "O(n+k)",     "O(n²)",      "O(n+k)",    True),
]


def print_complexity_table():
    header = f"  {'Algorithm':<16}  {'Best':<12}  {'Average':<12}  {'Worst':<12}  {'Space':<10}  Stable"
    print(header)
    print("  " + "-" * (len(header) - 2))
    for name, _, best, avg, worst, space, stable in ALGORITHMS:
        print(f"  {name:<16}  {best:<12}  {avg:<12}  {worst:<12}  {space:<10}  {'Yes' if stable else 'No'}")


def run_one(name, fn, sample, expected):
    start = time.perf_counter()
    result = fn(sample[:])
    elapsed = (time.perf_counter() - start) * 1000

    ok = result == expected
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {name:<16}  {elapsed:.3f} ms")
    if not ok:
        print(f"         input:    {sample}")
        print(f"         got:      {result}")
        print(f"         expected: {expected}")


def main():
    int_sample   = [random.randint(0, 99) for _ in range(12)]
    float_sample = [random.random() for _ in range(12)]
    expected_int   = sorted(int_sample)
    expected_float = sorted(float_sample)

    print("=" * 52)
    print("  SORTING ALGORITHM RUNNER")
    print("=" * 52)
    print(f"  Input (int):   {int_sample}")
    print(f"  Input (float): {[round(x, 3) for x in float_sample]}")
    print(f"  Expected Int:      {expected_int}")
    print(f"  Expected Float:  {expected_float}")
    print("-" * 52)

    for name, fn, *_ in ALGORITHMS:
        if fn is bucket_sort:
            run_one(name, fn, float_sample, expected_float)
        else:
            run_one(name, fn, int_sample, expected_int)

    print("=" * 52)
    print()
    print_complexity_table()
    print()
    print("  Run a single algorithm interactively:")
    print("  >>> from sorting_practice import merge_sort")
    print("  >>> merge_sort([5, 3, 1, 4, 2])")


if __name__ == "__main__":
    main()
