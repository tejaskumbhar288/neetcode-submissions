class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}

        def helper(k):
            if k not in memo:
                memo[k] = helper(k-1) + helper(k-2) + helper(k-3)
            return memo[k]

        return helper(n)