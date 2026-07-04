class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        my_dict = {}
        

        for c1, c2 in zip(s, t):
            if my_dict.get(c1):
                if my_dict[c1] != c2:
                    return False

            elif c2 in my_dict.values():
                return False
            else:
                my_dict[c1] = c2

        return True