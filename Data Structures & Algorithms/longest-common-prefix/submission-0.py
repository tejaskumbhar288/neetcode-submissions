class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs:
            pref = ""

            for c1, c2 in zip(prefix, s):
                if c1 == c2:
                    pref += c1
                else:
                    break

            prefix = pref

        return prefix