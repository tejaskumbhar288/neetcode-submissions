class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import defaultdict
        freq = defaultdict(int)

        for ch in text:
            if ch in "balon":
                freq[ch] += 1

        needed = ['b', 'a', 'l', 'o', 'n']
        for ch in needed:
            if ch not in freq:
                return 0

        #Since these characters appears twice
        freq['l'] //= 2
        freq['o'] //= 2

        return min(freq[c] for c in needed)