class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) == 0:
            return True

        if len(s) > len(t):
            return False
        
        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:
                i += 1

        return i == len(s)