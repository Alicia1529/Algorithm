```python
def maxWeight(n, weights, tasks, p):
    dp = []
    for i in range(n + 1):
        dp.append([0 for j in range(p + 1)])
    for i in range(1, n + 1):
        for j in range(1, p + 1):
            if j - 2 * tasks[i - 1] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 2 * tasks[i - 1]] + weights[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][p]
```