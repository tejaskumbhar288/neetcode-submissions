class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        if n == 1:
            return x

        if n == 0:
            return 1

        power_half = self.myPow(x, n//2)

        if n % 2 == 0:
            return power_half * power_half

        else:
            return x * power_half * power_half