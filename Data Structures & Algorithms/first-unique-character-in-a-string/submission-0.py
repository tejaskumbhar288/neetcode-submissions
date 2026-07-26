class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = {}
        for ch in s:
            my_dict[ch] = my_dict.get(ch, 0) + 1

        for i in range(len(s)):
            if my_dict[s[i]] == 1:
                return i

        return -1