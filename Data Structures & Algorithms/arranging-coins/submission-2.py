import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        #math formula -> O(1)
        # Use integer sqrt to avoid floating inaccuracies
        # Equivalent to floor((sqrt(1+8n)-1)/2)
        return (math.isqrt(1 + 8 * n) - 1) // 2
