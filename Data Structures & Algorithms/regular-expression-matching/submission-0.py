class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] = does s[i:] match p[j:]?
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True  # empty string matches empty pattern
        
        # Fill from bottom-right to top-left
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                # Check if current characters match
                match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                
                if j + 1 < len(p) and p[j + 1] == '*':
                    # Case 1: Skip "char*" (zero matches)
                    dp[i][j] = dp[i][j + 2]
                    # Case 2: If chars match, use '*' to match one more char
                    if match:
                        dp[i][j] = dp[i + 1][j] or dp[i][j]
                elif match:
                    # Normal match: consume both chars
                    dp[i][j] = dp[i + 1][j + 1]
        
        return dp[0][0]