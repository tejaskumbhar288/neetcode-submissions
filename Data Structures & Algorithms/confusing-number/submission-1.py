class Solution:
    def confusingNumber(self, n: int) -> bool:
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        original = n
        rotated = 0
        
        temp = n
        if n == 0: return False
        while temp > 0:
            digit = temp % 10
            if digit not in mapping:
                return False
            rotated = rotated * 10 + mapping[digit]
            temp //= 10

        return rotated != original