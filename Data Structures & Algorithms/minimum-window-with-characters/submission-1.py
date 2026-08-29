class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}

        for i in range(len(t)):
            need[t[i]] = need.get(t[i], 0) + 1

        required = len(need)
        have = 0
        left = 0
        best = ["", float('inf')] #(str, length)

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1

            while have == required:
                if best[1] > (right - left + 1):
                    substr = s[left: right + 1]
                    best[0] = substr
                    best[1] = len(substr)

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        if best[1] != float('inf'):
            return best[0]
        else:
            return ""
