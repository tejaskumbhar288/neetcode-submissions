class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastLength = 0
        temp = 0

        for i in range(len(s)):
            if (s[i] == ' '):
                if temp != 0:
                    lastLength = temp
                temp = 0

            else:
                temp += 1
                if i == (len(s) - 1):
                    lastLength = temp

        return lastLength