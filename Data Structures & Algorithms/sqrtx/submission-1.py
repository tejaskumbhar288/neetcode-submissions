class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x

        while left <= right:
            mid = (left + right) //2

            if (mid == x // mid) and (x % mid == 0):
                return mid
            elif (mid <= x // mid):
                left = mid + 1
            else:
                right = mid -1 

        return right

            