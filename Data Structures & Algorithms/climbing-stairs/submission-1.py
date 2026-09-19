class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def climb(n):
            if n <= 2:
                return n

            if n in dp:
                return dp[n]

            dp[n] = climb(n-1) + climb(n-2)

            return dp[n]

        return climb(n)

        