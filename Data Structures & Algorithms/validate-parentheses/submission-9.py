class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {']':'[', '}':'{', ')':'('}

        for ch in s:
            if ch in pairs:
                if not stack or pairs[ch] != stack[-1]:
                    return False
                else:
                    stack.pop()

            else:
                stack.append(ch)

        return not stack
            