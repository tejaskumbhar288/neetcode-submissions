class Solution:
    def rob(self, nums: List[int]) -> int:
        amount = 0
        n = len(nums)
        dp = {}

        def dfs(i):
            if i >= n:
                return 0

            if i in dp:
                return dp[i]

            dp[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return dp[i]

        return max(dfs(0), dfs(1))