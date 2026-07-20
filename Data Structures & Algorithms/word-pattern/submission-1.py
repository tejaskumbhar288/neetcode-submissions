class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        listed_s = s.split()

        pattern_check = {}
        if len(pattern) != len(listed_s):
            return False

        for i in range(len(pattern)):
            if pattern[i] in pattern_check:
                if pattern_check[pattern[i]] != listed_s[i]:
                    return False

            else:
                if listed_s[i] in pattern_check.values():
                    return False
                pattern_check[pattern[i]] = listed_s[i]

        return True
            