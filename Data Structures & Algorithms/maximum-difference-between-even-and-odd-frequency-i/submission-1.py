class Solution:
    def maxDifference(self, s: str) -> int:
        my_dict = {}
        for ch in s:
            my_dict[ch] = my_dict.get(ch, 0) + 1

        odd_max = 0
        even_min = len(s)

        for key in my_dict:
            if my_dict[key] % 2 == 0:
                even_min = min(even_min, my_dict[key])

            else:
                odd_max = max(odd_max, my_dict[key])

        return odd_max - even_min