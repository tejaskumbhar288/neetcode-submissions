from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #brute force
        count1 = Counter(s1)
        l1 = len(s1) 

        for i in range(l1, len(s2) + 1):
            substring = s2[i-l1 : i]
            count2 = Counter(substring)

            if count1 == count2:
                return True

        return False