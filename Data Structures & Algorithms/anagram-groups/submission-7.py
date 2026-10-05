from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        mydict = defaultdict(list)

        for s in strs:
            temp = "".join(sorted(s))
            mydict[temp].append(s)


        for key in mydict:
            result.append(mydict[key])

        return result