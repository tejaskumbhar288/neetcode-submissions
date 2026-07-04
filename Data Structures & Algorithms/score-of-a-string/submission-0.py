class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for i in range(1, len(s)):
            temp = (ord(s[i]) - ord(s[i-1]))
            if temp < 0:
                temp = -temp

            score += temp

        return score