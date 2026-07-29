class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n <= 2:
            return n
        # Alternatively, if n <= 3: return n works for n=3 as well

        prev2, prev1 = 1, 2  # ways for n=1 and n=2

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1