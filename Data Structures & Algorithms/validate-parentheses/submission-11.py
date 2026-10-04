class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {']': '[', '}': '{', ')': '('}

        for ch in s:
            if stack and ch in pairs:
                if pairs[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(ch)

        return not stack