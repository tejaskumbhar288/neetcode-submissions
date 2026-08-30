class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        stack = []

        for token in tokens:
            if token in "+-*/":
                second = stack[-1]
                stack.pop()
                first = stack[-1]
                stack.pop()
                temp = -1

                if token == "+":
                    temp = first + second

                elif token == "-":
                    temp = first - second
                
                elif token == "*":
                    temp = first * second

                elif token == "/":
                    if second != 0:
                        temp = int(first / second)


                stack.append(temp)

            else:
                stack.append(int(token))
        
        return stack[-1]

