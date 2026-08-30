class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []   # to store indices

        for i in range(len(temperatures)):
            while stack:
                top = stack[-1]
                if temperatures[i] > temperatures[top]:
                    stack.pop()
                    result[top] = (i - top)
                else:
                    break

                
            stack.append(i)

        return result
