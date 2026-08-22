# Binary Search

Overview
- Binary search is one idea — halve a search space on a **monotonic predicate** —
  wearing four disguises. The trick is recognizing which shape a problem is, then
  dropping in the matching template.
- The recurring bug is **never the idea, always the boundaries**. Almost every
  mistake is *mixing* two valid styles. Fix: make three independent decisions in
  order and keep each one internally consistent.

## The three independent decisions (do them in this order)

Mixing choices across these is the bug. Decide each one on its own.

| # | Decision | Driven by | Options |
|---|---|---|---|
| 1 | **Which template?** | exact match vs. boundary | B (exact) / A (boundary) |
| 2 | **Which loop pairing?** | fixed by #1 | `l<h`+`h=mid` / `l<=h`+`h=mid-1` |
| 3 | **Which init `high`?** | the answer range | `n-1` / `n` |

### 1 — Which template?
- Can you check `nums[mid] == target` and **return immediately**? → **Template B** (exact).
- Otherwise — *first / smallest* index where a condition flips, an insert position,
  a count, or "is answer X feasible?" → **Template A** (boundary).
- When unsure, **default to A**: it's the general tool (exact search is just A with
  `ok(mid) = nums[mid] >= target` plus an equality check afterward).
- **Tell for B:** the loop body has an `== target → return` line.

### 2 — Which loop pairing? (fixed by the template)
- **A:** `while l < h` + `h = mid` (keep) / `l = mid + 1` (exclude). Return `l`.
- **B:** `while l <= h` + `h = mid - 1` / `l = mid + 1`. Return `-1` if not found.
- **NEVER blend:** `l<=h` + `h=mid` → infinite loop; `l<h` + `h=mid-1` → skips the answer.
- The crux: whichever side *could still hold the answer* must not move past `mid`
  (use `h = mid`, not `mid - 1`).

### 3 — Which init `high`? (orthogonal to A vs B — driven by the answer range)
- Will you return `nums[left]` (answer is a real **element**, e.g. Find Min)? → `high = n-1`.
- Will you return `left` itself as an index/count where "past the end" is legal
  (insert position, `bisect_right`)? → `high = n`.
- Template A can use `n-1` — this choice is about *what you return*, not the loop shape.

---

## Template A — first index satisfying a predicate

```python
l, h = 0, n            # h = n if "past the end" is a legal answer, else n-1
while l < h:           # strict <  → pairs with h = mid
    mid = (l + h) // 2
    if ok(mid):        # mid MIGHT be the answer → keep it
        h = mid        # NOT mid - 1
    else:
        l = mid + 1
return l               # l == h == first index where ok() is True
```
- `ok()` must be **monotonic** (F,F,F,T,T,T). You find the first `T`.
- If nothing satisfies `ok`, returns `n` (or `h`) — check that after.

## Template B — classic exact search

```python
l, h = 0, n - 1
while l <= h:          # <= → pairs with mid - 1
    mid = (l + h) // 2
    if a[mid] == target: return mid
    elif a[mid] < target: l = mid + 1
    else:                 h = mid - 1
return -1
```

---

## Shape 1 — Search a sorted array (Template B)
Textbook exact match. **74. Search a 2D Matrix** — flatten the m×n grid to one
sorted array; map `idx → (idx // n, idx % n)` (divisor is `n`, the column count).

## Shape 2 — Broken-but-structured / rotated (predicate vs. an endpoint)
One half of `[l..mid..r]` is always sorted; compare against an endpoint.
- **153. Find Minimum in Rotated Sorted Array:** first index with `nums[mid] <= nums[-1]`.
  Template A, compare against `nums[right]` (handles the non-rotated case for free).
- **33. Search in Rotated Sorted Array:** Template B; use `nums[left] <= nums[mid]`
  to find which half is sorted, then check if target lies inside it.

## Shape 3 — Binary search on the answer (Template A) — top-3 FAANG Hard
The array isn't sorted, but "is candidate X feasible?" is monotonic F→T. Search the
*answer range*; the work is writing an O(n) greedy `feasible()`.
```python
def smallest_feasible(lo, hi):        # lo/hi = min/max possible answer
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid): hi = mid    # works → maybe smaller works
        else:             lo = mid + 1
    return lo
```
- **875. Koko Eating Bananas:** answer = speed in `[1, max(piles)]`;
  `feasible(s) = sum(ceil(p/s)) <= h`.
- **410. Split Array Largest Sum / 1011. Capacity to Ship:** answer = max allowed
  chunk sum in `[max(nums), sum(nums)]`; `feasible(cap) = greedy chunk count <= k`.

## Shape 4 — Search a partition (Template A) — capstone
**4. Median of Two Sorted Arrays:** binary-search the *cut position* `i` on the
*shorter* array (`m <= n`) so `i + j = half` and `maxLeft <= minRight` across both.
`j = half - i` is forced. Use ±inf for out-of-range boundaries. O(log(min(m,n))).

```python
if len(nums1) > len(nums2):              # always search the SHORTER array
    nums1, nums2 = nums2, nums1
m, n = len(nums1), len(nums2)
half = (m + n + 1) // 2                   # SIZE of the combined LEFT half
lo, hi = 0, m                            # cut position i ∈ [0, m] INCLUSIVE
while lo <= hi:
    i = (lo + hi) // 2                    # cut nums1 after i elements
    j = half - i                         # cut nums2 after j elements (forced)
    left1  = nums1[i-1] if i > 0 else float('-inf')
    right1 = nums1[i]   if i < m else float('inf')
    left2  = nums2[j-1] if j > 0 else float('-inf')
    right2 = nums2[j]   if j < n else float('inf')
    if left1 <= right2 and left2 <= right1:          # valid partition
        if (m + n) % 2: return max(left1, left2)     # odd → median in left half
        return (max(left1, left2) + min(right1, right2)) / 2   # even
    elif left1 > right2: hi = i - 1      # i too far right
    else:                lo = i + 1      # i too far left
```

**The ±1 rules — one mental model: "count vs. index" (个数 vs 下标).** Every offset
here is just this distinction; internalize it and you never memorize individual ±1s.

- **`i`, `j`, `half` are all COUNTS** (how many elements on the left). Same unit →
  add/subtract freely, **no ±1**. That's why `j = half - i` needs no adjustment.
- **`hi = m`, not `m-1`** — `i` is a cut *position*, not an index. A length-`m`
  array has `m + 1` cut positions (`0..m`); both extremes are valid (all of `nums1`
  on one side), so the range is inclusive → `hi = m`. (Same rule as `bisect_right`
  using `high = n`: you're searching a position/count, not an element index.)
- **`half = (m+n+1)//2`, not `(m+n)//2`** — `half` is a *count*, and "up to index
  k there are k+1 elements", so it's the median index **+ 1**. The `+1` puts the
  middle element in the left half on odd totals, so `max(left1, left2)` is the
  median. (Even totals: both formulas are equal.)
- **`nums1[i-1]`, `nums2[j-1]` use `-1`** — this is the *only* place you go from a
  COUNT back to an INDEX (the i-th element sits at index i-1). That conversion is
  where the `-1` belongs; the count-arithmetic above never needs it.

> Rule: **count↔count → no ±1; count→index (to fetch an element) → subtract 1.**
> The `+1` in `half` and the `-1` in `nums1[i-1]` are both count↔index conversions;
> `j = half - i` is count↔count, so it's clean.

An O(m+n) merge-walk (merge until the middle element) is far easier to read and
passes the judge, but it's *not* O(log) — in an interview it's the fallback, and
you'll be asked for this partition version.

---

## Common pitfalls (all the same bug)
- **Mixing the loop pairing** — `l<=h` with `h=mid` (infinite loop) or `l<h` with
  `h=mid-1` (skips the answer). This is the #1 recurring mistake.
- **Wrong init `high`** — a `bisect_right` / insert-position search needs `high = n`,
  not `n-1`, or the loop can never return `n` and the index underflows.
  *(Caught by `nums=[1], target=1` on 34 → returned `[0,-1]` instead of `[0,0]`.)*
- **Moving past a candidate** — on the keep-branch use `h = mid`, never `mid - 1`.
- **Non-monotonic `ok()`** — binary search only works if the predicate is F…FT…T.

## Related LeetCode problems
- [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) — the bare Template A / `bisect_left`
- [704. Binary Search](https://leetcode.com/problems/binary-search/) — the bare Template B
- [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
- [34. Find First and Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) — `bisect_left` + `bisect_right`
- [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)
- [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)
- [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
- [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
