class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        for s in words:
            for word in words:
                if word == s:
                    continue

                if s in word:
                    result.append(s)
                    break

        return result