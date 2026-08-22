# Union-Find (Disjoint Set Union)

Overview
- Tracks disjoint sets; supports `find(x)` and `union(a, b)`.
- Useful for connectivity, Kruskal, components.

Python (path compression + union by rank)
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

# Example:
# uf = UnionFind(5)
# uf.union(0,1); uf.union(1,2)
# uf.find(2) -> 0
```

## Union by rank
- `rank[x]` approximates the tree height or depth for root `x`.
- When two roots are united, attach the lower-rank tree under the higher-rank tree.
- This keeps the tree shallow and improves performance for future `find` calls.
- With path compression plus union by rank, the amortized time per operation is nearly constant (`O(α(n))`).
- When rank is not needed: for small inputs, one-shot unions, or when performance is not critical, you can skip rank and just attach one root to another.
- When rank is needed: for large inputs or many repeated union/find operations, rank (or size) avoids worst-case tall trees and keeps the structure efficient.
- For LeetCode examples like `323` and `547`, rank is optional because the algorithm performs a single controlled pass of unions over the given graph and correctness depends only on proper union/find, not tree height. In practice, the input size and structure keep performance acceptable, so path compression alone is enough for these cases.

## When to Use Union-Find vs DFS
- Use **Union-Find** when the problem focuses on connectivity or components and the input is naturally an edge list, or when you need to support repeated `union` operations followed by connectivity queries.
- Use **DFS** when you need to explore actual graph structure, traverse all neighbors, or when the graph is already represented as adjacency lists/matrices.
- Prefer **Union-Find** for problems with dynamic connectivity, multiple union operations, or when the only required output is the number of connected groups.
- Prefer **DFS** when you need path exploration, component-wise traversal order, or when the graph is small enough that recursion/traversal overhead is not a concern.

---

## Example: 323. Number of Connected Components in an Undirected Graph
Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges, return the number of connected components in the graph.

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.size = n
        parents = [i for i in range(n)]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return
            parents[root_a] = root_b
            self.size -= 1

        def find(a):
            if parents[a] != a:
                parents[a] = find(parents[a])
            return parents[a]

        for a, b in edges:
            union(a, b)
        return self.size
```

---

## Example: 547. Number of Provinces
Given an `n x n` adjacency matrix `isConnected` where `isConnected[i][j] = 1` means city `i` is directly connected to city `j`, return the number of connected provinces.

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.size = n
        parent = [i for i in range(n)]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j:
                return
            parent[root_j] = root_i
            self.size -= 1

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    union(i, j)
        return self.size
```

---

## Example: 261. Graph Valid Tree
Given `n` nodes labeled from `0` to `n-1` and a list of undirected edges, determine whether the graph is a valid tree.

```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[rb] < rank[ra]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
            return True

        for a, b in edges:
            if not union(a, b):
                return False
        return True
```

- `ra == rb` means the edge connects two nodes already in the same connected component, which forms a cycle.
- The check `len(edges) != n - 1` ensures that a connected tree must have exactly `n-1` edges.

---

## Example: 305. Number of Islands II
Given an `m x n` grid initialized with water, return the number of islands after each land addition in `positions`.

```python
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = dict()
        rank = dict()
        count = 0
        ans = []

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            nonlocal count
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            count -= 1

        for x, y in positions:
            if (x, y) in parent:
                ans.append(count)
                continue
            parent[(x, y)] = (x, y)
            rank[(x, y)] = 0
            count += 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighbor = (x + dx, y + dy)
                if neighbor in parent:
                    union((x, y), neighbor)
            ans.append(count)

        return ans
```

- Each new land starts as a separate island, then merges with adjacent lands if they belong to different components.
- Duplicate additions are skipped by checking whether the cell already exists in `parent`.
- Time: O(K × α(K)), Space: O(K) where K = number of positions.
