class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        my_map = {}
        n = len(words)
        for word in words:
            for ch in word:
                my_map[ch] = my_map.get(ch, 0) + 1

        for key in my_map:
            if not (my_map[key] % n == 0):
                return False

        return True