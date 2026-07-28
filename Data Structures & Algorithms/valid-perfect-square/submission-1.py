class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            square_num = (mid * mid)

            if  square_num == num:
                return True

            elif square_num < num:
                left = mid + 1

            else:
                right = mid - 1

        return False

            