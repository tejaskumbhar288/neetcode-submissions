class Solution:
    def maxDifference(self, s: str) -> int:
        my_dict = {}
        for ch in s:
            my_dict[ch] = my_dict.get(ch, 0) + 1

        odd_big = -float('inf')
        even_small = float('inf')

        for key in my_dict:
            if my_dict[key] % 2 == 0:
                even_small = min(even_small, my_dict[key])

            else:
                odd_big = max(odd_big, my_dict[key])

        return odd_big - even_small