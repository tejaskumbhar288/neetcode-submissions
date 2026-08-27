from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        result = []

        for s in strs:
            key = "".join(sorted(s))
            group[key].append(s)

        for key in group:
            result.append(group[key])

        return result