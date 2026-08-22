class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n, k = len(costs), len(costs[0])
        dp = costs[0][:]
        for i in range(1, n):
            new_dp = [0] * k
            for j in range(k):
                prev_costs = [dp[m] for m in range(k) if m != j]
                new_dp[j] = costs[i][j] + min(prev_costs)
            dp = new_dp
        return min(dp)