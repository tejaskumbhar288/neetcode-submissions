class Solution:
    def maxScore(self, s: str) -> int:
        zero_count = [0] * len(s)
        one_count = [0] * len(s)
        zeros = 0
        ones = 0

        for i in range(len(s)):
            ch = s[i]
            if ch == '0':
                zeros += 1
            zero_count[i] = zeros
            
        # print("zero count = ", zero_count)
        for i in range(len(s)-1, -1, -1):
            ch = s[i]
            if ch == '1':
                ones += 1
                
            one_count[i] = ones

        # print("One count = ", one_count)
        result = 0
        for i in range(len(s) - 1):
            result = max(result, zero_count[i] + one_count[i+1])

        return result
