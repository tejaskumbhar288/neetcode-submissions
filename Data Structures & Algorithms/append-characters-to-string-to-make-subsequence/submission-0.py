class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        if len(s) == 0:
            return len(t)

        for j in range(len(s)):
            if i < len(t) and s[j] == t[i]:
                i += 1

        return len(t) - i