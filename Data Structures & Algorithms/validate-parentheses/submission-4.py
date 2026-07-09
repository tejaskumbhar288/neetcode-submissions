class Solution:
    def isValid(self, s: str) -> bool:
        #Solution using stack
        stack = []
        inbracket = "([{"
        outbracket = ")]}"

        for c in s:
            if c in inbracket:
                stack.append(c)

            elif (c in outbracket and len(stack) > 0):
                top = stack[-1]
                if (c == ")" and top=="(") or (c == "]" and top=="[") or (c == "}" and top=="{"):
                    stack.pop()

                else:
                    return False

            else:
                return False

            print(stack)

        return len(stack) == 0