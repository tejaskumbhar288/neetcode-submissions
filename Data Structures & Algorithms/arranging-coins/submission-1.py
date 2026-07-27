class Solution:
    def arrangeCoins(self, n: int) -> int:
        #brute force
        sum = n
        result = 0
        if n==1:
            return 1

        for i in range(1, n):
            if sum < i:
                return result

            sum -= i
            result += 1

        return result
