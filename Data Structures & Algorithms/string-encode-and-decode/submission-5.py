class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):

            j = s.find("#", i)

            if j == -1:
                break

            length = int(s[i:j])

            temp_s = s[j+1: j + length + 1]
            result.append(temp_s)
            i = j + 1 + length

        return result