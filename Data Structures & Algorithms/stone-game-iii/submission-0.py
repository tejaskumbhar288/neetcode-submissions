class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)  # dp[i] = best net advantage for current player starting at i

        for i in range(n - 1, -1, -1):
            take = 0
            best = float("-inf")

            # Try taking 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k > n:
                    break
                take += stoneValue[i + k - 1]
                best = max(best, take - dp[i + k])

            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"