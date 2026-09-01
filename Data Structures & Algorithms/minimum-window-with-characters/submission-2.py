class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        left = 0
        have = 0
        need = {}
        best = ["", float('inf')]
        window = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        required = len(need)

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1

            while have == required:
                if (right-left +1 ) < best[1]:
                    best[0] = s[left: right+1]
                    best[1] = right-left+1

                lc = s[left]
                window[lc] -= 1

                if lc in need and window[lc] < need[lc]:
                    have -= 1

                left += 1


        if best[1] != float('inf'):
            return best[0]
        else:
            return ""



