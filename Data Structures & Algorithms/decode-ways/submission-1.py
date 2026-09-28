class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def dfs(i):
            #successfully consumed complete string
            if i == len(s):
                return 1

            #A number cannot start with 0
            if s[i] == '0':
                return 0

            if i in memo:
                return memo[i]

            #take one digit
            ways = dfs(i+1)

            #take two digit if valid
            if (i + 1) < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i + 2)

            memo[i] = ways
            return ways

        return dfs(0)


