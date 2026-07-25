class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        length = 0
        odd_exists = False
        for count in freq.values():
            length += (count // 2) * 2
            if count % 2 == 1:
                odd_exists = True
        
        return length + (1 if odd_exists else 0)