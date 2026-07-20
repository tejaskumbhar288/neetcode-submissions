class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        my_dict = {}
        for ch in chars:
            my_dict[ch] = my_dict.get(ch, 0) + 1

        total = 0

        for word in words:
            contains = True
            for ch in word:
                if word.count(ch) > my_dict.get(ch, 0):
                    contains = False
                    break

            if contains:
                total += len(word)

        return total