# LeetCode Study Plan — by Topic

**Profile:** Solid on Mediums, weak on Hards · Target: FAANG / Big Tech

**Goal:** Pattern mastery + Hard-problem fluency + interview reflexes

Organized by topic (not by day). Each section holds its **Progress** log and
**Pattern Knowledge**. Work any section in any order; spaced-repeat every miss.

---

## Core Strategy

You already *can* solve problems. The two things that actually move the needle:

1. **Pattern recognition speed** — see a problem, name the pattern in <60 seconds.
2. **Hard-problem decomposition** — Hards are almost always 2 patterns stacked, or a Medium + an optimization. Train this explicitly.

**Don't do this:** grind 200 random problems. **Do this:** ~5–7 problems, deeply understood, with spaced repetition on every miss.

**Session rhythm (3–4 hrs):**
- 30 min — review previously-missed problems (no peeking)
- 90 min — 3–4 new problems on one pattern
- 45 min — 1 Hard problem, even if you don't fully solve it
- 30 min — read editorials/discuss section for elegant solutions you missed

---

## Patterns Ranked by FAANG Frequency

| Tier | Pattern | Why it matters |
|---|---|---|
| S | Arrays & Hashing | Appears in 40%+ of phone screens |
| S | Two Pointers / Sliding Window | High-frequency, easy to mess up edge cases |
| S | BFS / DFS on Trees & Graphs | Onsite staple |
| S | Dynamic Programming | The Hard-problem killer; expect 1 per onsite |
| A | Binary Search (incl. binary search on answer) | Trick variant shows up constantly |
| A | Heap / Priority Queue | Top-K, scheduling, merging |
| A | Backtracking | Combinatorial generation |
| A | Intervals | Meeting rooms, merging |
| A | Stack / Monotonic Stack | Next-greater, histogram problems |
| B | Trie | Word search, autocomplete |
| B | Union-Find | Connectivity, MST |
| B | Topological Sort | Course schedule family |
| B | Greedy | Often a Medium dressed as Hard |
| C | Bit Manipulation | Occasional flavor problem |
| C | Math / Geometry | Rare but unmissable when it shows |

---

## Arrays, Hashing, Two Pointers
- **Mediums:** Group Anagrams · Top K Frequent Elements · Product of Array Except Self · 3Sum · Container With Most Water
- **Hard:** Trapping Rain Water *(two pointers — start here, it's the gentlest Hard)*
- **Drill:** Re-derive prefix-sum and hashing-for-O(1)-lookup from scratch.

#### Progress — Arrays, Hashing, Two Pointers

- [x] 15. 3Sum ✓ — solved 2026-05-25

**Hashmap**
- [x] 383. Ransom Note ✓ — solved 2026-06-23
- [x] 205. Isomorphic Strings ✓ — solved 2026-06-23
- [x] 290. Word Pattern ✓ — solved 2026-06-23
- [x] 242. Valid Anagram ✓ — solved 2026-06-23
- [x] 49. Group Anagrams ✓ — solved 2026-06-23
- [x] 1. Two Sum ✓ — solved 2026-06-23
- [x] 202. Happy Number ✓ — solved 2026-06-23
- [x] 219. Contains Duplicate II ✓ — solved 2026-06-23
- [x] 128. Longest Consecutive Sequence ✓ — solved 2026-06-23
- [x] 238. Product of Array Except Self ✓ — solved 2026-06-24 · prefix/suffix products, O(1) extra space
- [x] 169. Majority Element ✓ — solved 2026-07-04 · Boyer-Moore voting (cancel opposing votes), O(n)/O(1)
- [x] 14. Longest Common Prefix ✓ — solved 2026-07-04 · vertical scan, bound by shortest string, O(S)
- [x] 189. Rotate Array ✓ — solved 2026-07-05 · 3 reversals (foolproof) · cyclic replacement w/ gcd(n,k) cycles + counter, O(n)/O(1)

**Two Pointers**
- [x] 125. Valid Palindrome ✓ — solved 2026-06-24
- [x] 392. Is Subsequence ✓ — solved 2026-06-24
- [x] 167. Two Sum II - Input Array Is Sorted ✓ — solved 2026-06-24
- [x] 11. Container With Most Water ✓ — solved 2026-06-24
- [x] 15. 3Sum ✓ (re-solved) — solved 2026-06-24
- [x] 88. Merge Sorted Array ✓ — solved 2026-06-28, 2026-08-30 · fill from the back — write head `k` never outruns read head `i`, O(m+n)/O(1)
- [x] 80. Remove Duplicates from Sorted Array II ✓ — solved 2026-08-30 · compare vs `nums[k-2]` (the kept window) — generalizes to "at most m" via `k-m`, O(n)/O(1)

**Heap / Quickselect**
- [x] 347. Top K Frequent Elements ✓ — solved 2026-06-24 · 3 approaches: size-K heap (N log K) · heapify+pop (N + K log N) · quickselect (N avg)

**Hard**
- [x] 42. Trapping Rain Water ✓ — solved 2026-06-24 · prefix/suffix DP · two-pointer O(1) · monotonic stack

#### Pattern Knowledge — Arrays, Hashing & Two Pointers

**The core trade you're always making:** spend O(n) *space* (a hash map/set) to buy O(1) *time*
on lookups, turning an O(n²) brute force into O(n). "Have I seen X before?" / "what's the
count/index of X?" → reach for a hash structure.

---

**1. Hashing — the three jobs a dict/set does**

| Job | Structure | Trigger phrase |
|---|---|---|
| "Have I seen this?" / dedup | `set` | "contains duplicate", "first unique" |
| "How many of each?" | `Counter` / dict of counts | "anagram", "frequency", "k most common" |
| "Where did I see it?" (need the index/partner) | dict `value -> index` | "two sum", "subarray summing to k" |

**Complement pattern (Two Sum family) — the #1 hashing trick:**
> Instead of trying every pair O(n²), for each `x` ask "have I already seen `target - x`?"
> Store each number's index as you go; the partner, if it exists, is already in the map.
```python
seen = {}                          # value -> index
for i, x in enumerate(nums):
    if target - x in seen:         # complement already seen → done
        return [seen[target - x], i]
    seen[x] = i
```

**Frequency / anagram pattern:**
```python
from collections import Counter
Counter(s) == Counter(t)           # valid anagram in O(n)

# Group anagrams: bucket by a canonical key (sorted string, or 26-char count tuple)
groups = defaultdict(list)
for w in words:
    key = tuple(sorted(w))         # or a 26-length count signature
    groups[key].append(w)
```

**Bijection pattern (Isomorphic Strings / Word Pattern):** a one-to-one mapping needs *two*
dicts (or check both directions) — mapping `a→x` is not enough; you must also forbid `b→x`.
```python
def is_iso(s, t):
    fwd, bwd = {}, {}
    for a, b in zip(s, t):
        if fwd.setdefault(a, b) != b or bwd.setdefault(b, a) != a:
            return False
    return True
```

**Set-membership for O(n) scans (Longest Consecutive Sequence):** dump into a set, then only
start counting from a *sequence start* (`num-1 not in set`) so each run is walked once → O(n).

---

**2. Two Pointers — when the array structure lets two indices replace a nested loop**

| Flavor | Setup | Use case |
|---|---|---|
| Opposite ends | `l=0, r=n-1`, move inward | sorted Two Sum, Container With Most Water, valid palindrome |
| Same direction (fast/slow) | both start left, advance at different rates | remove duplicates in-place, cycle detection, sliding window |
| Sort + scan + inner two-pointer | sort, fix one, two-pointer the rest | 3Sum, 4Sum |

**Opposite-ends template (requires sorted input):**
```python
l, r = 0, len(nums) - 1
while l < r:
    total = nums[l] + nums[r]
    if total == target: return [l, r]
    elif total < target: l += 1        # need bigger → move left pointer up
    else:                r -= 1         # need smaller → move right pointer down
```
> Why it works: sortedness means moving `l` right can only *increase* the sum and moving `r`
> left can only *decrease* it — so each step provably eliminates no valid answer.

**3Sum = sort + fix one + two-pointer the rest** (the canonical "Hard = Medium + a layer"):
```python
nums.sort()
for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i-1]:     # skip duplicate anchors
        continue
    l, r = i + 1, len(nums) - 1
    while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s < 0:   l += 1
        elif s > 0: r -= 1
        else:
            res.append([nums[i], nums[l], nums[r]])
            l += 1; r -= 1
            while l < r and nums[l] == nums[l-1]: l += 1   # skip dup
            while l < r and nums[r] == nums[r+1]: r -= 1
```

---

**3. Prefix Sum — answer range queries / "subarray summing to k" in O(n)**

> `prefix[i]` = sum of the first `i` elements. Then `sum(i..j) = prefix[j+1] - prefix[i]`.
> Combine with a hash map of seen prefix sums to count subarrays with a target sum.
```python
# Subarray Sum Equals K — O(n)
count, cur = 0, 0
seen = {0: 1}                      # empty prefix
for x in nums:
    cur += x
    count += seen.get(cur - k, 0)  # how many earlier prefixes make this window == k
    seen[cur] = seen.get(cur, 0) + 1
```

**Product of Array Except Self** — prefix/suffix passes, no division: build left-products,
then multiply by right-products in a second pass. Same "precompute a running aggregate" idea.

---

**Decision checklist:**

| Signal in problem | Pattern |
|---|---|
| "Have I seen…", "duplicate", "frequency", "anagram" | Hash set / Counter |
| "Two numbers that sum to…", pair with a target | Hash complement (unsorted) or two pointers (sorted) |
| "Triplets / quadruplets summing to…" | Sort + fix + two pointers |
| Sorted array, find pair/window | Two pointers (opposite ends) |
| In-place dedup, partition | Two pointers (fast/slow) |
| "Sum of subarray", "range sum", "subarray == k" | Prefix sum (+ hash map) |
| "Product/aggregate except self" | Prefix/suffix arrays |

---

## Sliding Window
- **Mediums:** Longest Substring Without Repeating Characters · Longest Repeating Character Replacement · Permutation in String · Min Size Subarray Sum
- **Hard:** Minimum Window Substring · Sliding Window Maximum
- **Drill:** Write the canonical "expand right, shrink left" template once and never look at it again.

#### Progress — Sliding Window

- [x] 3. Longest Substring Without Repeating Characters ✓ — solved 2026-05-31 ⚠️ O(N) optimized solution (jump `l` directly via hashmap index, `max(l, cache[s[r]]+1)`) not fully understood — prioritize on review
- [x] 28. Find the Index of the First Occurrence in a String ✓ — solved 2026-06-24 · brute-force sliding window O(n·m)

---

## Matrix
- **Mediums:** Spiral Matrix · Rotate Image · Set Matrix Zeroes · Diagonal Traverse · Search a 2D Matrix
- **Drill:** Layer/boundary bookkeeping — most matrix bugs are single-row/column rings and shrinking bounds. Guard every "walk back" pass with a "is there still a row/col left?" check.

#### Progress — Matrix

- [x] 54. Spiral Matrix ✓ — solved 2026-07-05 · peel rings (recursive) / shrink 4 boundaries (iterative); guard bottom+left with `height>1 and width>1`, O(m·n)
- [x] 48. Rotate Image ✓ — solved 2026-07-05 · transpose + reverse rows (canonical) / ring rotation cycling 4 cells, in-place O(n²)
- [x] 723. Candy Crush ✓ — solved 2026-07-05 · simulation find→crush→drop loop; collect crush cells in a SET (simultaneous), gravity via write pointer, O((m·n)²)

#### Pattern Knowledge — Matrix

**The core patterns (most → least common):**

**1. Boundary / layer traversal (Spiral, 54)** — walk in rings, shrinking four
bounds (`top/bottom/left/right`). The bug is always the **single-row / single-col
ring** — guard every "walk back" pass with "is there still a row/col left?".

**2. Transpose + reverse (Rotate Image, 48)** — rotate 90° clockwise = **transpose,
then reverse each row**.
```python
n = len(matrix)
for i in range(n):
    for j in range(i + 1, n):                    # transpose — upper triangle ONLY
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for row in matrix:
    row.reverse()                                # then flip each row
```
> `j` starts at `i+1` — transposing the whole matrix swaps every pair twice and
> undoes itself. Counterclockwise = transpose + reverse each *column*.

**3. First row/col as marker storage (Set Matrix Zeroes, 73)** — need O(1) space and
would normally use a `seen` set? **Store flags in the matrix itself** — use row 0 /
column 0 as "should this row/col be zeroed?" bookkeeping (handle the `[0][0]` overlap
+ a separate `col0` flag). "Encode state in the structure you're given."

**4. Grid DFS/BFS (Islands, Flood Fill, Word Search)** — the universal skeleton:
```python
DIRS = ((1,0), (-1,0), (0,1), (0,-1))
def neighbors(r, c):
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:    # the universal bounds check
            yield nr, nc
```

**5. Sorted-matrix search** — **74** (globally sorted): flatten to 1D, binary search,
`idx → (idx//n, idx%n)`, O(log(mn)). **240** (rows/cols sorted, not global): start at
the **top-right corner**, go left if too big / down if too small, O(m+n).

---

**Transferable tips:**

- **Index mapping** — `2D→1D: idx = r*n + c`; `1D→2D: r,c = idx//n, idx%n`. The
  divisor is always **`n` (columns)**, never `m`. (This bit you on 74.)
- **Direction vectors** — always write dirs as `(dr, dc)` tuples and loop; never
  hand-write four `if` branches.
- **Rows vs cols discipline** — `m, n = len(matrix), len(matrix[0])` (m=rows,
  n=cols). Half of all matrix bugs are `matrix[c][r]` typos. Say "row first, column
  second" out loud.
- **O(1)-space in-place tricks:** encode flags in row0/col0 (73) · transpose+reverse
  instead of copying (48) · mark visited by mutating the cell then restore (Word
  Search: set `'#'`, restore on backtrack).
- **Turning / direction changes:** `DIRS=[(0,1),(1,0),(0,-1),(-1,0)]` (R,D,L,U) and
  `d = (d+1) % 4` to turn clockwise.
- **Diagonals:** cells on the same diagonal share `r-c`; same anti-diagonal share
  `r+c`. Group by that to solve Diagonal Traverse (498) and any "process diagonals".

---

**Pattern-recognition table:**

| Problem says… | Reach for |
|---|---|
| "spiral", "traverse in order", "layers" | Boundary shrinking + single-row/col guard |
| "rotate the image 90°" | Transpose + reverse rows |
| "set entire row/col to zero", O(1) space | First row/col as markers |
| "islands", "regions", "flood", "reachable" | Grid DFS/BFS + bounds check |
| "sorted matrix", search for target | 74: flatten + binary search · 240: top-right corner walk |
| "path top-left → bottom-right", count/min | 2D DP (`dp[i][j]` from top/left neighbors) |
| "diagonal" | Group by `r+c` (anti-diagonal) or `r-c` (diagonal) |

---

## Stack & Monotonic Stack
- **Mediums:** Daily Temperatures · Car Fleet · Evaluate Reverse Polish Notation · Valid Parentheses
- **Hard:** Largest Rectangle in Histogram · ~~Maximal Rectangle~~ *(skipped — revisit later)*
- **Drill:** Monotonic stack template — when do you pop? When do you push the index vs. value?

#### Progress — Stack & Monotonic Stack
- [x] 496. Next Greater Element I ✓ — solved 2026-04-30
- [x] 503. Next Greater Element II ✓ — solved 2026-04-30
- [x] 739. Daily Temperatures ✓ — solved 2026-04-30
- [x] 853. Car Fleet ✓ — solved 2026-05-01 ⚠️ not fully understood — prioritize on review
- [x] 150. Evaluate Reverse Polish Notation ✓ — solved 2026-05-01
- [x] 20. Valid Parentheses ✓ — solved 2026-05-01
- [x] 84. Largest Rectangle in Histogram ✓ — solved 2026-05-01 ⚠️ not fully confident — prioritize on review

#### Pattern Knowledge — Stack & Monotonic Stack

**When to reach for a stack:**
- You need to process elements in LIFO order
- "Most recent unseen" / "waiting for a future event" — classic stack trigger
- Balanced brackets, function call simulation, undo operations

**When to reach for a monotonic stack:**
- "Next greater / next smaller element" to the right or left
- Any question that asks about the *nearest* element satisfying a condition
- Histogram / rectangle problems (think: what is each bar's reach?)

**The core mental model:**
> Imagine people standing in a line, each looking right for the first person taller than them.
> The stack holds people still *waiting*. When you meet someone taller, everyone shorter finally has their answer — pop and record.

**Two flavors:**

| Flavor | Stack property | Pop condition | Use case |
|---|---|---|---|
| Monotonic decreasing | top is smallest | `num > stack[-1]` | Next Greater Element |
| Monotonic increasing | top is largest | `num < stack[-1]` | Next Smaller Element |

**Template (Next Greater, going left→right):**
```python
stack = []   # stores elements waiting for their answer
result = {}

for num in nums:
    while stack and stack[-1] < num:   # num is the answer for stack top
        result[stack.pop()] = num
    stack.append(num)

# remaining in stack → no greater element exists → -1
```

**Template (index variant — used when you need distances, e.g. Daily Temperatures):**
```python
stack = []   # stores *indices*, not values
result = [0] * len(nums)

for i, num in enumerate(nums):
    while stack and nums[stack[-1]] < num:
        j = stack.pop()
        result[j] = i - j          # distance to next greater
    stack.append(i)
```

**Worked example — Next Greater Element:**
```
nums = [2, 1, 5, 3]

i=0, num=2 → stack: [2]
i=1, num=1 → 1 < 2, push → stack: [2, 1]
i=2, num=5 → 5 > 1, pop → result[1]=5; 5 > 2, pop → result[2]=5; push → stack: [5]
i=3, num=3 → 3 < 5, push → stack: [5, 3]

Remaining [5, 3] → result = -1
Final: {2:5, 1:5, 5:-1, 3:-1}
```

**Key decision checklist:**
1. Do I need the *value* or the *index*? (index when distances matter)
2. Am I looking left or right? (right → iterate forward; left → iterate backward or use a suffix pass)
3. Increasing or decreasing monotone? (greater → decreasing stack; smaller → increasing stack)
4. Is the array circular? → **expand the list**: iterate `2n` times using `nums[i % n]`. This simulates wrapping around without actually duplicating the array.

```python
# Circular variant (503. Next Greater Element II)
n = len(nums)
result = [-1] * n
stack = []  # stores indices

for i in range(2 * n):        # go around twice
    while stack and nums[stack[-1]] < nums[i % n]:
        result[stack.pop()] = nums[i % n]
    if i < n:                 # only push indices from the first pass
        stack.append(i)
```

---

## Binary Search (including on answer)

Binary search isn't one trick — it's four recognizable shapes on a **monotonic
predicate**. Learn to spot which shape a problem is, then drop in the matching
template. Order them easiest → hardest and do at least 2 of the answer-space ones
(top-3 FAANG Hard pattern).

- **Shape 1 · Search a sorted array** — the textbook case. *Search a 2D Matrix
  (74)* (flatten the grid to one sorted array). Exact-match Template B.
- **Shape 2 · Search a broken-but-structured array** — sorted then rotated, so one
  half is always sorted. *Find Minimum in Rotated Sorted Array (153)* → *Search in
  Rotated Sorted Array (33)*. Predicate compares against an endpoint.
- **Shape 3 · Binary search on the answer** — the array isn't sorted, but
  "is candidate X feasible?" is monotonic F→T. Search the *answer range*; the work
  is writing an O(n) greedy `feasible()`. *Koko Eating Bananas (875)* → *Split Array
  Largest Sum (410)* (a.k.a. *Capacity to Ship 1011*). **← spend the most time here.**
- **Shape 4 · Search a partition** — *Median of Two Sorted Arrays (4)*, the
  capstone: binary-search the cut point on the shorter array. Hardest edge handling.

**Context / why this matters:** almost every FAANG "make it faster than O(n)" or
"minimize the maximum / maximize the minimum" prompt is secretly one of Shapes 3–4.
The recurring failure isn't the idea — it's **loop boundaries**. The guide below
pins every shape to exactly two templates so the boundaries stop biting you.

> Full reference (three-decision cheat sheet + all four shapes + templates):
> `Collections/Binary Search.md`.

#### Guide — Binary Search

**The one rule that fixes your recurring bug.** Every boundary mistake comes from
mixing two *valid* styles. Pin every binary search to ONE of these and never blend
them. The crux: *whichever side could still contain the answer must not move past
`mid`.*

**Template A — find first index satisfying a predicate** (your default; use for
almost everything, including "on the answer"):

```python
l, h = 0, n            # h = n when "past the end" is a legal answer, else n-1
while l < h:           # NOTE: strict <, and half-open
    mid = (l + h) // 2
    if ok(mid):        # mid MIGHT be the answer → keep it
        h = mid        # do NOT do mid - 1
    else:
        l = mid + 1
return l               # l == h == first index where ok() is True
```

- `while l < h` **pairs with** `h = mid`. Loop shrinks every step (mid < h when
  l < h), so no infinite loop. Terminates with `l == h`.
- `ok()` must be **monotonic**: F,F,F,T,T,T. You're finding the first `T`.
- If no index satisfies `ok`, this returns `n` (or `h`) — check that after.

**Template B — classic exact search** (only when you want an exact match / not a
boundary):

```python
l, h = 0, n - 1
while l <= h:          # <= pairs with mid - 1
    mid = (l + h) // 2
    if a[mid] == target: return mid
    if a[mid] < target:  l = mid + 1
    else:                h = mid - 1
return -1
```

The forbidden combos (this is the bug): `l <= h` **with** `h = mid` → infinite
loop; `l < h` **with** `h = mid - 1` → skips the answer.

---

**Binary search on the answer space** — the top-3 Hard pattern. When the array
isn't what's sorted but the *answer* is monotonic ("is candidate X feasible?"
flips F→T at the smallest good X), search over the answer range with Template A:

```python
def smallest_feasible(lo, hi):        # lo/hi = min/max possible answer
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid): hi = mid    # mid works → maybe smaller works too
        else:             lo = mid + 1
    return lo
```

The whole trick is **writing `feasible(mid)`** — usually an O(n) greedy pass.

- **Koko Eating Bananas (875):** answer = eating speed, range `[1, max(piles)]`.
  `feasible(speed) = sum(ceil(p/speed) for p) <= h`. Find smallest feasible speed.
- **Split Array Largest Sum (410) / Capacity to Ship (1011):** answer = the max
  allowed subarray sum, range `[max(nums), sum(nums)]`.
  `feasible(cap) = greedy count of chunks needed <= k`. Find smallest feasible cap.

---

**The rotated-array problems** — Template A, but the predicate compares against an
endpoint (there's no fixed sorted order to bisect on directly):

- **Find Minimum in Rotated Sorted Array (153):** the min is the first index whose
  value is `<= nums[-1]`. So `ok(mid) = nums[mid] <= nums[-1]`, Template A, return
  `nums[l]`. (Assumes distinct + actually rotated; a fully sorted array still works
  since everything is `<= nums[-1]`.)
- **Search in Rotated Sorted Array (33):** `while l <= h`; at each `mid`, exactly
  one half `[l..mid]` or `[mid..h]` is sorted — detect with `nums[l] <= nums[mid]`,
  then check if target lies inside that sorted half to decide which way to go.
- **Search a 2D Matrix (74):** treat the m×n grid as one sorted array of length
  `m*n`; map index `i → (i // n, i % n)` and run plain Template B.

---

**Median of Two Sorted Arrays (4)** — the Hard capstone. Don't merge (that's O(n)).
Binary-search the *partition point* on the **shorter** array so that
`left_A + left_B` = half the total, with `maxLeft <= minRight` across both. Range
is `[0, len(shorter)]`, Template A. Get the four boundary values right (use ±inf
for out-of-range) and this is O(log(min(m,n))). Expect to get it wrong twice — the
edge handling is the whole difficulty; write out a 4-element example by hand first.

---

**Interview checklist**
- State your invariant out loud: "the answer is always in `[l, h)`."
- Pick Template A unless you specifically need exact-match B.
- Use `mid = (l + h) // 2` (Python bigints — no overflow to worry about).
- Confirm `ok()` is monotonic before you code, and sanity-check the return when
  *nothing* satisfies the predicate.
- Trace one tiny example (2–3 elements) to prove the loop terminates.

#### Progress — Binary Search

- [x] 33. Search in Rotated Sorted Array ✓ — solved 2026-06-29 · one half always sorted, `nums[left] <= nums[mid]`, Template B
- [x] 35. Search Insert Position ✓ — solved 2026-06-29 · find first index with `nums[i] >= target`, Template A
- [x] 74. Search a 2D Matrix ✓ — solved 2026-06-29 · flatten to length m·n, `i=idx//n, j=idx%n`, Template B
- [x] 162. Find Peak Element ✓ — solved 2026-06-29 · move toward the larger neighbor, `nums[mid] < nums[mid+1] → l=mid+1`, Template A ⚠️ needs review
- [x] 34. Find First and Last Position ✓ — solved 2026-06-29 · bisect_left + bisect_right, Template A ⚠️ needs review — failed `[1]`,tgt=1: bisect_right must init `high=n` not `n-1`
- [x] 153. Find Minimum in Rotated Sorted Array ✓ — solved 2026-06-29 · first index `<= nums[-1]`, Template A ⚠️ needs review — slipped `left<right`+`right=mid` pairing
- [x] 4. Median of Two Sorted Arrays ✓ — solved 2026-07-04 · partition cut on shorter array, `j=half-i`, count-vs-index ±1 rule; also kth-smallest w/ indices (clamp + actual-discard-count) ⚠️ needs review
- [x] 875. Koko Eating Bananas ✓ — solved 2026-07-05 · binary search on answer, `feasible(k)=sum(ceil(p/k))<=h`, range `[1,max]`, Template A

---

## Linked Lists + Trees (BFS/DFS)
- **Mediums:** Reorder List · Remove Nth Node · Copy List with Random Pointer · LCA of BST · Validate BST · Kth Smallest in BST · Construct Tree from Preorder+Inorder
- **Hard:** Binary Tree Maximum Path Sum · Serialize/Deserialize Binary Tree
- **Drill:** Recursive tree DP template — "what does each subtree return to its parent?"

#### Progress — Linked Lists + Trees

- [x] 21. Merge Two Sorted Lists ✓ — solved 2026-06-28 · dummy head, two pointers, splice remainder, O(m+n)/O(1)
- [x] 124. Binary Tree Maximum Path Sum ✓ — solved 2026-06-22

---

## Heap + Intervals + Greedy
- **Mediums:** Kth Largest Element · Task Scheduler · Insert Interval · Non-overlapping Intervals · Meeting Rooms II · Jump Game · Gas Station
- **Hard:** Find Median from Data Stream · Merge K Sorted Lists
- **Drill:** Two-heap pattern (median stream) — memorize it cold.

#### Progress — Heap + Intervals + Greedy

- [x] 23. Merge k Sorted Lists ✓ — solved 2026-06-28 · min-heap of list heads, pop smallest, O(N log k)
- [x] 253. Meeting Rooms II ✓ — solved 2026-05-31 ⚠️ not comfortable — prioritize on review
- [x] 55. Jump Game ✓ — solved 2026-08-31 · greedy reachability frontier, `max_reach = max(max_reach, i + nums[i])`, fail when `max_reach < i`, O(n)
- [x] 45. Jump Game II ✓ — solved 2026-08-31 · BFS-by-levels without the queue — `current_end` closes a level, `farthest` opens the next, O(n)
- [x] 56. Merge Intervals ✓ — solved 2026-09-02 · sort by start, extend with `max` (nested intervals!), `<=` merges touching, O(n log n)
- [x] 57. Insert Interval ✓ — solved 2026-09-02 · input pre-sorted → 3 phases (before / merge / after); binary-search the two boundaries to make it ~flat
- [x] 452. Minimum Number of Arrows to Burst Balloons ✓ — solved 2026-09-02 · sort by **end**, shoot at `points[0][1]`, new arrow only when `last_shoot < start` (`<` — touching balloons share an arrow)

#### Pattern Knowledge — Greedy

**When greedy works:** a *local* rule provably gives the global optimum, so you never
need to store per-index state. The tell: DP would work but the recurrence collapses
into a single running `max`/`min`.

**1. Reachability frontier (Jump Game, 55)** — carry the farthest index reachable so
far; if the frontier ever falls behind where you stand, there's an uncrossable gap.
```python
max_reach = 0
for i in range(len(nums)):
    if max_reach < i:            # CHECK BEFORE UPDATE
        return False
    max_reach = max(max_reach, i + nums[i])
return True
```
> Order matters. Update first and a `0` at index `i` extends the frontier from a
> square you never reached. Backward variant: shrink the target — `if i + nums[i] >=
> last: last = i`, reachable iff `last == 0`.

**2. Frontier + level counting (Jump Game II, 45)** — same scan, but count *minimum*
jumps: it's BFS by levels flattened into one pass. Close a level when `i` reaches the
previous frontier.
```python
jumps = cur_end = farthest = 0
for i in range(len(nums) - 1):        # stop before last — arriving needs no new jump
    farthest = max(farthest, i + nums[i])
    if i == cur_end:                  # exhausted this level
        jumps += 1
        cur_end = farthest
return jumps
```

**3. Running-best scan (Best Time to Buy/Sell Stock, 121)** — keep min-so-far, take
the best difference against it. Same shape: one accumulator, no table.

**4. Sort, then take greedily (intervals)** — the sort key IS the algorithm, and it
differs per question:

| Problem | Sort key | Why |
|---|---|---|
| 56. Merge Intervals | **start** | build groups left→right; only the right edge matters |
| 57. Insert Interval | **start** (given sorted) | 3 phases: copy before · merge · copy after |
| 435. Non-overlapping | **end** | keeping the earliest-ending one leaves the most room |
| 452. Burst Balloons | **end** | same scan as 435, but touching **shares** an arrow (`s > end`, not `s >= end`) |
| 253. Meeting Rooms II | **start** + min-heap of ends | sweep the timeline |

> Swapping these genuinely breaks both directions — 56 sorted by end gives
> `[[0,2],[1,1]] → [[1,2]]`; 435 sorted by start removes 3 instead of 2 on
> `[[1,100],[11,22],[1,11],[2,12]]`. Two merge traps: extend with **`max`** (a nested
> interval would shrink the group) and use **`<=`** (touching counts as overlapping —
> check the problem statement, this is the #1 silent wrong answer).

> **The trap:** greedy fails the moment a locally worse choice can pay off later
> (Coin Change with arbitrary denominations). If you can't state *why* the local rule
> is safe, write the DP.

---

## Backtracking
- **Mediums:** Combination Sum · Permutations · Subsets · Word Search · Palindrome Partitioning · Letter Combinations of a Phone Number
- **Hard:** N-Queens · Word Search II *(combine with Trie)*
- **Drill:** Backtracking template — when do you copy the path vs. push the reference?

#### Progress — Backtracking
- [x] 46. Permutations ✓ — solved 2026-05-01
- [x] 77. Combinations ✓ — solved 2026-05-01
- [x] 17. Letter Combinations of a Phone Number ✓ — solved 2026-05-01
- [x] 39. Combination Sum ✓ — solved 2026-05-01
- [x] 22. Generate Parentheses ✓ — solved 2026-05-02
- [x] 79. Word Search ✓ — solved 2026-05-02 · re-solved 2026-06-21
- [ ] 208. Implement Trie *(prerequisite for 212 — see Advanced Graphs + Tries)*
- [ ] 212. Word Search II *(requires Trie — see Advanced Graphs + Tries)*

#### Pattern Knowledge — Backtracking

**When to use:**
- "Generate all..." / "Find all combinations / permutations / subsets"
- Constraint satisfaction — build a solution step by step, abandon it the moment it violates a constraint

**Mental model:**
> You're exploring a decision tree. At each node you make a choice, go deeper, then **undo** that choice and try the next one. The undo step is what makes it backtracking.

**Universal template:**
```python
def backtrack(start, path):
    if is_solution(path):
        result.append(path[:])   # snapshot — NOT a reference
        return
    for choice in choices(start):
        path.append(choice)      # choose
        backtrack(next, path)    # explore
        path.pop()               # undo
```

**Three key decisions:**

| Question | Answer |
|---|---|
| Copy or reference? | Always `path[:]` or `path.copy()` when appending to result — never the live list |
| `start` or `0`? | Pass `start=i+1` to avoid reuse (combinations); pass `start=0` with a `visited` set for permutations |
| When to prune? | Add `if len(path) > limit` or `if remaining < 0` at the top — cuts branches early |

**The four classic shapes:**

```
Subsets      → include or skip each element, no start constraint
Combinations → pick k from n, iterate from start (no duplicates)
Permutations → all orderings, use visited[] to track used indices
Partitions   → split string/array, recurse on suffix
```

**Handling duplicates** (e.g. Combination Sum II):
```python
nums.sort()  # must sort first
for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i-1]:  # skip duplicate at same level
        continue
```

**Time complexity:** O(2ⁿ) for subsets, O(n!) for permutations — don't optimize, just prune.

---

## Graphs (BFS/DFS, Union-Find, Topo Sort)
- **Mediums:** Number of Islands · Clone Graph · Pacific Atlantic · Course Schedule (I & II) · Number of Connected Components · Redundant Connection
- **Hard:** Word Ladder · Alien Dictionary
- **Drill:** Implement Union-Find with path compression + union by rank from scratch. You will need it.

#### Progress — Graphs

**Grid BFS/DFS** *(easiest entry — 2D arrays)*
- [x] 733. Flood Fill ✓ — solved 2026-06-11
- [x] 200. Number of Islands ✓ — solved 2026-06-11
- [x] 695. Max Area of Island ✓ — solved 2026-06-11
- [x] 1254. Number of Closed Islands ✓ — solved 2026-06-11
- [x] 994. Rotting Oranges ✓ — solved 2026-06-11 ⚠️ off-by-one on BFS depth (count levels that actually rot, or guard `while queue and fresh`) — prioritize on review

**Explicit graphs (adjacency list)** *(nodes numbered, edges given as pairs)*
- [x] 997. Find the Town Judge ✓ — solved 2026-06-12
- [x] 133. Clone Graph ✓ — solved 2026-06-12
- [x] 547. Number of Provinces ✓ — solved 2026-06-12
- [x] 841. Keys and Rooms ✓ — solved 2026-06-12

**Topological sort & cycle detection**
- [x] 207. Course Schedule ✓ — solved 2026-06-12
- [x] 210. Course Schedule II (medium) — output the topological order ✓ — solved 2026-06-13

**Union-Find** *(sets up Islands II)*
- [x] 323. Number of Connected Components (medium) — union-find intro ✓ — solved 2026-06-15, 2026-06-18, 2026-06-23
- [x] 261. Graph Valid Tree (medium) ✓ — solved 2026-06-15, 2026-06-18, 2026-06-23
- [x] 305. Number of Islands II (hard) — union-find capstone ✓ — solved 2026-06-15, 2026-06-18, 2026-06-23

> **Memorize first:** grid DFS (733/200/695/1254) and topological sort (207/210). Most graph problems are variations of these two.

#### Pattern Knowledge — Graphs

**Graph Representations:**
```python
# Adjacency list (most common in LC)
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # undirected
```

**BFS** — shortest path in unweighted graph, minimum steps/hops, level-by-level traversal:
```python
from collections import deque

queue = deque([start])
visited = set([start])
steps = 0

while queue:
    for _ in range(len(queue)):   # process one level at a time
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    steps += 1
```

**DFS** — connectivity, cycle detection, path existence, flood fill:
```python
# Recursive
def dfs(node, visited, graph):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph)

# Iterative
def dfs(start, graph):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            stack.append(neighbor)
```

**Union-Find** — connectivity queries, cycle detection in undirected graphs, "same group?":
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False   # already connected → cycle detected
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px           # union by rank
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
```

**Topological Sort (Kahn's — BFS-based)** — ordering with dependencies, course prerequisites:
```python
from collections import deque, defaultdict

def topo_sort(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(n) if indegree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == n else []  # empty → cycle exists
```

**Topological Sort (DFS — post-order):**
```python
def dfs(node):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)
    order.append(node)      # add AFTER exploring neighbors
# reverse order at end → topological order
```

**Cycle Detection:**

| Graph type | Method |
|---|---|
| Undirected | Union-Find (`union` returns False = cycle) |
| Directed | 3-color DFS (white/gray/black) or Kahn's (`len(order) != n`) |

**3-color DFS for directed cycle:**
```python
# 0 = unvisited, 1 = in-progress, 2 = done
def dfs(node):
    state[node] = 1
    for neighbor in graph[node]:
        if state[neighbor] == 1: return True   # back edge → cycle
        if state[neighbor] == 0 and dfs(neighbor): return True
    state[node] = 2
    return False
```

**Decision checklist:**

| Signal in problem | Pattern |
|---|---|
| "Shortest path", "minimum steps" | BFS |
| "Does path exist", "connected components" | DFS or Union-Find |
| "Number of islands" / flood fill | DFS/BFS on grid |
| "Prerequisites", "ordering tasks" | Topological Sort (Kahn's) |
| "Redundant connection", "same group" | Union-Find |
| Directed graph + cycle detection | 3-color DFS or Kahn's |

---

## Dynamic Programming I (1D)
- **Mediums:** House Robber (I & II) · Decode Ways · Coin Change · Word Break · Longest Increasing Subsequence · Partition Equal Subset Sum
- **Hard:** Best Time to Buy and Sell Stock IV · Frog Jump
- **Drill:** Always write the recurrence in English first. Then translate to code. Memo first, tabulate only if asked.

#### Progress — Dynamic Programming (1D)

- [x] 509. Fibonacci Number ✓ — solved 2026-05-25
- [x] 70. Climbing Stairs ✓ — solved 2026-05-30
- [x] 322. Coin Change ✓ — solved 2026-05-30
- [x] 300. Longest Increasing Subsequence ✓ — solved 2026-05-31
- [x] 354. Russian Doll Envelopes ✓ — solved 2026-05-31
- [x] 121. Best Time to Buy and Sell Stock ✓ — solved 2026-05-31, 2026-06-24
- [x] 122. Best Time to Buy and Sell Stock II ✓ — solved 2026-05-31

#### Pattern Knowledge — Dynamic Programming (1D)

**When to use:**

- "Maximum / minimum / count" over a sequence of choices
- "Can we achieve X?" (boolean feasibility)
- Brute force is exponential but subproblems repeat → overlapping subproblems + optimal substructure

**Mental model:**
> Decompose into smaller subproblems. Cache each answer so you never solve it twice. Build the final answer from cached results.

**The 4-step framework:**
1. **Define state** — `dp[i]` = "answer considering the first i elements"
2. **Write the recurrence** — express `dp[i]` in terms of smaller states
3. **Identify base cases** — the smallest states you know without computing
4. **Determine order** — usually left-to-right; verify each state only depends on already-computed states

**Top-down template (memoization — start here):**
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(i):
    if i == 0: return base_value
    return min/max/sum(dp(i-1), dp(i-2), ...)
```

**Bottom-up template (tabulation):**
```python
dp = [0] * (n + 1)
dp[0] = base
for i in range(1, n + 1):
    dp[i] = f(dp[i-1], dp[i-2], ...)
```

**Common 1D patterns:**

| Problem | State | Recurrence |
|---|---|---|
| House Robber | dp[i] = max money from first i houses | `max(dp[i-1], dp[i-2] + nums[i])` |
| Coin Change | dp[i] = min coins for amount i | `min(dp[i-c]+1 for c in coins if c<=i)` |
| LIS | dp[i] = LIS length ending at index i | `max(dp[j]+1 for j<i if nums[j]<nums[i])` |
| Word Break | dp[i] = can form s[:i] from dict | `any(dp[j] and s[j:i] in wordDict for j<i)` |
| Decode Ways | dp[i] = ways to decode s[:i] | `dp[i-1] if valid 1-digit + dp[i-2] if valid 2-digit` |

**Decision checklist:**
1. Can I express the answer as a function of a smaller subproblem? → DP
2. What choices do I make at each step? → These define the recurrence
3. What uniquely identifies a subproblem? → This is your state
4. Does `dp[i]` depend on only a few previous states? → Can space-optimize to O(1)

---

## Dynamic Programming II (2D + Knapsack + Strings)
- **Mediums:** Unique Paths · Longest Common Subsequence · Edit Distance · Target Sum · Coin Change II
- **Hard:** Regular Expression Matching · Wildcard Matching · Distinct Subsequences · Burst Balloons
- **Drill:** This is *the* topic. Most candidates break here. Do at least 2 Hards even if painful.

#### Progress — Dynamic Programming (2D)

- [x] 764. Largest Plus Sign ✓ — solved 2026-06-27 · 4 directional run-length sweeps, dp = min(4 arms), O(n²)
- [x] 1434. Number of Ways to Wear Different Hats ✓ — solved 2026-07-05 · bitmask DP, compress people (`2^n`) iterate hats, `dp(hat,mask)` ⚠️ not familiar — prioritize on review

#### Pattern Knowledge — Dynamic Programming (2D + Knapsack)

**2D state:** `dp[i][j]` = answer considering first i elements of one thing and first j of another

**LCS / Edit Distance template:**
```python
dp = [[0] * (n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if s1[i-1] == s2[j-1]:          # characters match
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = 1 + min(dp[i-1][j],    # delete
                                dp[i][j-1],    # insert
                                dp[i-1][j-1])  # replace
```

**0/1 Knapsack — each item used at most once:**
```python
# 2D
dp = [[0]*(W+1) for _ in range(n+1)]
for i in range(1, n+1):
    for w in range(W+1):
        dp[i][w] = dp[i-1][w]                               # skip item i
        if weights[i-1] <= w:
            dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])  # take it

# Space-optimized 1D — MUST iterate w right→left
dp = [0] * (W+1)
for i in range(n):
    for w in range(W, weights[i]-1, -1):   # ← right-to-left prevents reuse
        dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
```

**Unbounded Knapsack — item reuse allowed (Coin Change II):**
```python
dp = [0] * (amount+1)
dp[0] = 1
for coin in coins:
    for w in range(coin, amount+1):        # ← left-to-right allows reuse
        dp[w] += dp[w-coin]
```

**⚠️ The one thing that kills people:**

| Type | Inner loop direction | Why |
|---|---|---|
| 0/1 knapsack | right → left | prevents using item twice |
| Unbounded knapsack | left → right | allows reusing item |

**Common 2D patterns:**

| Problem | State | Key transition |
|---|---|---|
| Unique Paths | dp[i][j] = paths to (i,j) | `dp[i-1][j] + dp[i][j-1]` |
| LCS | dp[i][j] = LCS of s1[:i], s2[:j] | match: `dp[i-1][j-1]+1`, else: `max(dp[i-1][j], dp[i][j-1])` |
| Partition Equal Subset | dp[i][s] = can reach sum s using first i | 0/1 knapsack |
| Target Sum | dp[i][s] = ways to reach sum s at index i | `dp[i-1][s-nums[i]] + dp[i-1][s+nums[i]]` |

---

## Advanced Graphs + Tries
- **Mediums:** Implement Trie · Design Add and Search Words · Network Delay Time *(Dijkstra)* · Cheapest Flights Within K Stops *(Bellman-Ford)*
- **Hard:** Swim in Rising Water · Reconstruct Itinerary · Min Cost to Connect All Points *(MST)*
- **Drill:** Dijkstra template with heap. Know when Bellman-Ford is required (negative weights, k-stops).

#### Progress — Advanced Graphs + Tries

**Trie**
- [x] 208. Implement Trie (Prefix Tree) (medium) — the foundation; build it cold ✓ — solved 2026-06-21
- [x] 211. Design Add and Search Words Data Structure (medium) — Trie + DFS for the `.` wildcard ✓ — solved 2026-06-21
- [x] 212. Word Search II (hard) — Trie + grid backtracking *(the canonical Trie capstone)* ✓ — solved 2026-06-21 ⚠️ needs review — prioritize on review

**Shortest path (weighted)**
- [ ] 743. Network Delay Time (medium) — Dijkstra intro
- [ ] 787. Cheapest Flights Within K Stops (medium) — Bellman-Ford / Dijkstra with a hop limit
- [ ] 778. Swim in Rising Water (hard) — Dijkstra on a grid (minimize the max edge)

**Minimum spanning tree & Eulerian path**
- [ ] 1584. Min Cost to Connect All Points (medium/hard) — Prim's or Kruskal's MST
- [ ] 332. Reconstruct Itinerary (hard) — Hierholzer's algorithm (Eulerian path)

> **Memorize first:** the Trie node + insert/search (208) and the Dijkstra heap template. 212 and 778 are just those two ideas wearing a costume.

#### Pattern Knowledge — Trie (Prefix Tree)

**When to reach for a Trie:**
- Many strings sharing prefixes — autocomplete, spell-check, dictionary lookup
- "Does any word start with this prefix?" (a hash set of words *can't* answer prefix queries efficiently)
- You'll query the same dictionary repeatedly — pay O(total chars) to build once, then O(word length) per query
- Wildcard / partial matching over a word list (211)
- Pruning a search: while DFS-ing a grid, abandon a path the instant its prefix isn't in the Trie (212)

**Mental model:**
> A tree where each *edge* is a character and each *path from the root* spells a prefix. Words that share a prefix share the same path until they diverge. A boolean flag marks where a complete word ends.

**The core structure:**
```python
class TrieNode:
    def __init__(self):
        self.children = {}        # char -> TrieNode  (or [None]*26 for a-z only)
        self.is_word = False      # True if a word ends exactly here
```

**Trie template (208 — insert / search / startsWith):**
```python
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True          # mark the end of a complete word

    def _walk(self, prefix):         # shared helper: returns the node or None
        node = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.is_word   # must be a *complete* word

    def startsWith(self, prefix):
        return self._walk(prefix) is not None      # prefix existing is enough
```

**⚠️ The one distinction that trips people up:**
> `search` requires `is_word == True` (the word must actually end there).
> `startsWith` only requires the path to *exist*. Conflating these is the #1 Trie bug.

**Wildcard search (211 — `.` matches any character):**
When you hit a `.`, you can't pick a branch — you must try *all* children. That turns the linear walk into a DFS.
```python
def search(self, word):
    def dfs(node, i):
        if i == len(word):
            return node.is_word
        c = word[i]
        if c == '.':
            return any(dfs(child, i + 1) for child in node.children.values())
        if c not in node.children:
            return False
        return dfs(node.children[c], i + 1)
    return dfs(self.root, 0)
```

**Trie + backtracking (212 — Word Search II):**
The key insight: instead of running Word Search once per word (O(W · cells · 4^L)), build **one Trie of all words**, then DFS the grid *once*, walking the Trie in lockstep. The instant the current grid path isn't a Trie prefix, prune.
```python
def findWords(self, board, words):
    root = TrieNode()
    for w in words:                      # build one Trie of all target words
        node = root
        for c in w:
            node = node.children.setdefault(c, TrieNode())
        node.word = w                    # store the full word at its end node

    res, rows, cols = [], len(board), len(board[0])

    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node.children:      # prefix not in Trie → prune entire branch
            return
        nxt = node.children[ch]
        if nxt.word:                     # found a complete word
            res.append(nxt.word)
            nxt.word = None              # de-dup: don't report the same word twice
        board[r][c] = '#'                # mark visited
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                dfs(nr, nc, nxt)
        board[r][c] = ch                 # restore (backtrack)

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    return res
```

**Complexity:**

| Operation | Time | Space |
|---|---|---|
| insert / search / startsWith | O(L) — L = word length | O(total chars) for the whole Trie |
| Build Trie of N words | O(N · L) | O(N · L) worst case (no shared prefixes) |

**Trie decision checklist:**
1. Are there *many* strings and repeated *prefix* queries? → Trie (a hash set only answers exact membership).
2. Wildcards or "match any char"? → Trie + DFS, branch on every child at the `.`.
3. Searching a grid/space against a *word list*? → one Trie, DFS once, prune on missing prefix.
4. `a–z` only and memory matters? → use `children = [None]*26` instead of a dict (faster, less overhead).
5. Need to report or delete whole words? → store the word (or a count) on the terminal node, not just a bool.

#### Pattern Knowledge — Weighted Graphs (Dijkstra · Bellman-Ford · MST)

**Which algorithm?**

| Signal in problem | Algorithm |
|---|---|
| Shortest path, **non-negative** weights | Dijkstra (heap) |
| Negative weights, or "at most K edges/stops" | Bellman-Ford |
| Connect all nodes at **minimum total cost** | MST (Prim's / Kruskal's) |
| Use **every edge exactly once** (itinerary) | Hierholzer's (Eulerian path) |
| Unweighted shortest path | plain BFS (don't reach for Dijkstra) |

**Dijkstra (heap) — shortest path from a source, non-negative weights:**
```python
import heapq

def dijkstra(graph, start, n):          # graph: node -> [(neighbor, weight)]
    dist = {i: float('inf') for i in range(n)}
    dist[start] = 0
    heap = [(0, start)]                  # (distance_so_far, node)

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:               # stale entry — already finalized
            continue
        for nei, w in graph[node]:
            if d + w < dist[nei]:        # found a shorter path
                dist[nei] = d + w
                heapq.heappush(heap, (d + w, nei))
    return dist
```
> **Why the `d > dist[node]` skip?** We never decrease-key the heap; we just push duplicates. The first time we pop a node it's finalized — later (larger) copies are stale and skipped.

**Bellman-Ford — handles negative weights & a hop limit (787, Cheapest Flights ≤ K stops):**
Relax all edges K+1 times. Snapshot `dist` each round so a path can't use more than one new edge per round.
```python
def find_cheapest(n, flights, src, dst, k):
    dist = [float('inf')] * n
    dist[src] = 0
    for _ in range(k + 1):               # at most k stops = k+1 edges
        snapshot = dist[:]               # ← use last round's values only
        for u, v, w in flights:
            if snapshot[u] + w < dist[v]:
                dist[v] = snapshot[u] + w
    return dist[dst] if dist[dst] != float('inf') else -1
```

**Dijkstra on a grid — Swim in Rising Water (778), minimize the *max* edge:**
Same heap, but the "distance" is the **max elevation** seen so far along the path, not a sum.
```python
def swim(grid):
    n = len(grid)
    heap = [(grid[0][0], 0, 0)]          # (max_elevation_so_far, r, c)
    seen = {(0, 0)}
    while heap:
        t, r, c = heapq.heappop(heap)
        if (r, c) == (n - 1, n - 1):
            return t
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                seen.add((nr, nc))
                heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
```

**MST — Prim's (heap-based), Min Cost to Connect All Points (1584):**
Grow a tree from any node, always pulling the cheapest edge crossing to an unvisited node.
```python
def min_cost(points):
    n = len(points)
    heap = [(0, 0)]                      # (cost, node) — start at node 0
    seen = set()
    total = 0
    while len(seen) < n:
        cost, u = heapq.heappop(heap)
        if u in seen:
            continue
        seen.add(u)
        total += cost
        for v in range(n):
            if v not in seen:
                d = abs(points[u][0]-points[v][0]) + abs(points[u][1]-points[v][1])
                heapq.heappush(heap, (d, v))
    return total
```
> **Kruskal's alternative:** sort all edges, add the cheapest that doesn't form a cycle (use Union-Find from the Graphs section). Prefer Prim's on dense graphs, Kruskal's when edges are given as a sorted-able list.

**Eulerian path — Reconstruct Itinerary (332), Hierholzer's:**
Use every ticket exactly once. Greedily walk to the smallest-lexicographic destination; when stuck, append to the route and backtrack. The route comes out reversed.
```python
def find_itinerary(tickets):
    graph = defaultdict(list)
    for u, v in sorted(tickets, reverse=True):   # reverse → pop() gives smallest
        graph[u].append(v)
    route = []
    def dfs(node):
        while graph[node]:
            dfs(graph[node].pop())
        route.append(node)               # add on the way *out* (post-order)
    dfs("JFK")
    return route[::-1]
```

**Complexity cheat sheet:**

| Algorithm | Time | Note |
|---|---|---|
| Dijkstra (heap) | O(E log V) | non-negative weights only |
| Bellman-Ford | O(V · E) | handles negatives; K-stop variant is O(K · E) |
| Prim's (heap) | O(E log V) | MST |
| Kruskal's | O(E log E) | MST, needs Union-Find |
| Hierholzer's | O(E) | Eulerian path/circuit |

---

## Math / Geometry

#### Progress — Math / Geometry

- [x] 7. Reverse Integer ✓ — solved 2026-06-24
- [x] 50. Pow(x, n) ✓ — solved 2026-07-05 · fast power `xⁿ=(x^(n/2))²`, compute half ONCE (decrement→halve), O(log n)

---

## Design

#### Progress — Design

- [x] 380. Insert Delete GetRandom O(1) ✓ — solved 2026-06-27 · hashmap (val→idx) + array + swap-with-last for O(1) remove
- [x] 146. LRU Cache ✓ — solved 2026-06-27, 2026-06-28 · hashmap + doubly-linked list w/ dummy head/tail, O(1) get/put
- [x] 460. LFU Cache ✓ — solved 2026-06-28 · key2val + freq→OrderedDict[key] + minFrequency, O(1) get/put

---

## Hard-Problem Decomposition Framework

When you see a Hard, run this in your head before coding:

1. **What's the brute force?** Always state it. Often O(n²) or O(2ⁿ).
2. **What's redundant in the brute force?** Recomputation? → DP. Repeated scanning? → two pointers / sliding window. Sorted/monotonic structure? → binary search / monotonic stack.
3. **What pattern does the simplified version match?** Strip the Hard down to a Medium and ask "if the constraint were smaller, what would I do?"
4. **What's the optimization layer?** Hards usually = Medium pattern + one of: memoization, monotonic structure, binary search on answer, two-heap, segment tree, prefix/suffix arrays.

Practice this *out loud* — your interviewer judges your process more than your final code.

---

## The "Patterns Cheat Sheet" You Build Yourself

Keep a single doc. For each pattern, fill in:

- **Trigger phrases** in the problem statement (e.g., "find the longest contiguous…" → sliding window)
- **Canonical template** (your own version, not copy-pasted)
- **Top 2 problems** that exemplify it
- **Edge cases** that bit you

This becomes your pre-interview review document.

---

## Mock Interview Resources

- **Pramp** — free, peer-to-peer, decent
- **interviewing.io** — paid but with real FAANG engineers
- **Yourself in front of a whiteboard, talking out loud** — underrated; the speaking-while-coding muscle is what fails first under pressure

Do full mocks regularly — the more the better.

---

## Day-of-Interview Behavior

1. **Clarify for 60–90 seconds.** Input ranges. Duplicates? Sorted? Negative numbers? Empty input? Return type?
2. **State a brute force first**, even if obvious. Then optimize. Don't jump to optimal — interviewers want to see the *path*.
3. **Talk while coding.** Silence reads as "stuck."
4. **Test on the example, then a tiny edge case** (empty, single element, all-same).
5. **State final time/space complexity** unprompted.

---

## Tracking Template

| Topic | Mediums Done | Hard Done | Got Stuck On | Re-do Date |
|---|---|---|---|---|
| Arrays/Hashing (hashmap) | 383 Ransom Note ✓ · 205 Isomorphic Strings ✓ · 290 Word Pattern ✓ · 242 Valid Anagram ✓ · 49 Group Anagrams ✓ · 1 Two Sum ✓ · 202 Happy Number ✓ · 219 Contains Duplicate II ✓ · 128 Longest Consecutive Sequence ✓ · 238 Product of Array Except Self ✓ | 42 Trapping Rain Water ✓ | — | 2026-06-25 |
| Two Pointers | 125 Valid Palindrome ✓ · 392 Is Subsequence ✓ · 167 Two Sum II ✓ · 11 Container With Most Water ✓ · 15 3Sum ✓ | — | — | 2026-06-26 |
| Heap / Quickselect | 347 Top K Frequent Elements ✓ | — | — | 2026-06-26 |
| Sliding Window | 4 | Min Window Substring | Shrink condition | — |
| Stack / Monotonic Stack | 496 Next Greater Element I ✓ · 503 Next Greater Element II ✓ · 739 Daily Temperatures ✓ · 853 Car Fleet ✓ · 150 Evaluate Reverse Polish Notation ✓ · 20 Valid Parentheses ✓ | 84 Largest Rectangle in Histogram ✓ | — | 853 Car Fleet ⚠️ · 84 Largest Rectangle in Histogram ⚠️ |
| Trees (DFS) | — | 124 Binary Tree Maximum Path Sum ✓ | — | — |
| Backtracking | 46 Permutations ✓ · 77 Combinations ✓ · 17 Letter Combinations ✓ · 39 Combination Sum ✓ · 22 Generate Parentheses ✓ · 79 Word Search ✓ | — | — | 79 Word Search ⚠️ |
| Graphs (grid BFS/DFS) | 733 Flood Fill ✓ · 200 Number of Islands ✓ · 695 Max Area of Island ✓ · 1254 Number of Closed Islands ✓ · 994 Rotting Oranges ✓ | — | 994 BFS depth off-by-one | 994 Rotting Oranges ⚠️ |
| Graphs (explicit + topo) | 997 Find the Town Judge ✓ · 133 Clone Graph ✓ · 547 Number of Provinces ✓ · 841 Keys and Rooms ✓ · 207 Course Schedule ✓ | — | — | — |
| Trie | 208 Implement Trie ✓ · 211 Add and Search Words ✓ | 212 Word Search II ✓ | — | 212 Word Search II ⚠️ |
| Weighted Graphs | 743 Network Delay (Dijkstra) · 787 Cheapest Flights (Bellman-Ford) · 1584 Connect All Points (MST) | 778 Swim in Rising Water · 332 Reconstruct Itinerary | — | — |

The "Re-do Date" column matters most. Spaced repetition (re-solve at +2, +5, +10 days) is the single biggest delta between people who pass and don't.

---

Good luck. Pattern recognition + calm decomposition + spoken process. That's the whole game.
