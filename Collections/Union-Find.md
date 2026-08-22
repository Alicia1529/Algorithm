# Union-Find (Disjoint Set)

Overview
- Union-Find (Disjoint Set Union, DSU) keeps track of a partition of elements into disjoint sets. It supports two operations:
  - `find(x)`: return a representative (root) of the set containing `x`.
  - `union(a, b)`: merge the sets containing `a` and `b`.

Heuristics
- Path compression: during `find`, point nodes directly to the root to flatten the tree.
- Union-by-rank or union-by-size: attach the smaller tree under the larger one to keep height low.

Why it helps
- With both heuristics, operations are nearly constant time (amortized O(α(n))).

Use case: LeetCode 261 — Graph Valid Tree
- Solution idea: an undirected graph is a tree iff it's connected and acyclic. While processing edges with Union-Find, if an edge connects two nodes that already share the same root, it creates a cycle.
- See the full problem notes and alternative solutions: [Leetcode/261. Graph Valid Tree.md](Leetcode/261.%20Graph%20Valid%20Tree.md)

Python implementation (concise, robust):
```python
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[rb] < self.rank[ra]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # quick reject: tree with n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
        dsu = DSU(n)
        for a, b in edges:
            if not dsu.union(a, b):
                return False  # cycle detected
        return True
```

Notes
- `union` returns `False` when an edge closes a cycle (both endpoints already connected).
- You can also track `components` (start at `n`, decrement on successful `union`) and check `components == 1` instead of the `n-1` edges check.

Complexity
- Time: O(m * α(n)) where m = number of edges.
- Space: O(n) for `parent` and `rank` arrays.
