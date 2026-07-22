class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x: float, n: int) -> float:
            if x == 0:          # edge case
                return 0
            if n == 0:
                return 1

            # Recursively compute (x*x)^(n//2)
            half = helper(x * x, n // 2)
            # If n is odd, multiply by one extra x
            return x * half if n % 2 else half

        # Handle negative exponent by taking reciprocal
        result = helper(x, abs(n))
        return result if n >= 0 else 1.0 / result