class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
            
        result = n & (n-1)
        return result == 0