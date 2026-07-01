class Solution:
    def isValid(self, s: str) -> bool:
        temp = []

        for c in s:
            if c in "([{":
                temp.append(c)
            
            else:
                if not temp:
                    return False
                    
                sample = temp.pop()
                
                if c == ')' and sample != '(':
                    return False
                elif c == ']' and sample != '[':
                    return False
                elif c == '}' and sample != '{':
                    return False

            
        return len(temp) == 0

            