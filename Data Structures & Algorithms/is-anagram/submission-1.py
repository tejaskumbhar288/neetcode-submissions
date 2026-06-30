class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        if len(s) != len(t):
            return False

        for ch in s:
            my_dict[ch] = my_dict.get(ch, 0) + 1

        for ch in t:
            if my_dict.get(ch):
                my_dict[ch] -= 1

            else:
                return False

        return True

        