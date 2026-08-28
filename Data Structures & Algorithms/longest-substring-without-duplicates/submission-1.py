class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #dict based
        last_seen = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in last_seen:
                last_seen.pop(s[left])
                left += 1

            last_seen[s[right]] = right
            longest = max(longest, right-left+1)

        return longest