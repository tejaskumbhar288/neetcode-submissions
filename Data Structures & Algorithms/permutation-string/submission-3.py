class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        need = {}
        have = {}
        matches = 0
        n = len(s1)

        for ch in s1:
            need[ch] = need.get(ch, 0) + 1
            
        required = len(need)

        for right in range(len(s2)):
            c = s2[right]
            have[c] = have.get(c, 0) + 1
            if c in need and have[c] == need[c]:
                matches += 1

            if right - left + 1 > n:
                lc = s2[left]
                if lc in need and have[lc] == need[lc]:
                    matches -= 1
                have[lc] -= 1
                if have[lc] == 0:
                    del have[lc]
                left += 1

            if matches == required:
                return True


        return False
