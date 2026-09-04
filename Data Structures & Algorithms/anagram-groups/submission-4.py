from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        result = []

        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        for key in groups:
            result.append(groups[key])
        return result
