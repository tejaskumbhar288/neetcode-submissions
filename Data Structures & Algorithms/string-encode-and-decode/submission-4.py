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
            length = int(s[i:j])
            temp = s[j+1 : j + 1 + length]
            result.append(temp)

            i = j + 1 + length

        return result
