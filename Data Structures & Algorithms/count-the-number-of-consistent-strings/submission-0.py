class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        my_dict = {}
        for ch in allowed:
            my_dict[ch] = my_dict.get(ch, 0) + 1

        total = 0

        for word in words:
            contains = True
            for ch in word:
                if ch not in my_dict:
                    contains = False
                    break

            if contains:
                total += 1

        return total