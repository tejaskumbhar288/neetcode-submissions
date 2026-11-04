class Solution:
    def isHappy(self, n: int) -> bool:
        def square_digit(n):
            result = 0

            while n > 0:
                digit = n % 10
                result += digit * digit
                n = n // 10

            return result

        my_dict = {}

        def is_cyclic(n):
            nonlocal my_dict

            square_num = square_digit(n)

            if square_num == 1:
                return True

            if square_num in my_dict:
                return False

            my_dict[square_num] = 1
            return is_cyclic(square_num)

        return is_cyclic(n)

