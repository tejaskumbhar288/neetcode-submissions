class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            temp = ''.join(sorted(s))
            result[temp].append(s)

        return list(result.values())