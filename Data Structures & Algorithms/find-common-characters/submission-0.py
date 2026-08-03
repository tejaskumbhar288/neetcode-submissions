class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Start with the first word's character counts
        cnt = Counter(words[0])

        # Intersect counts with each subsequent word
        for w in words[1:]:
            cur_cnt = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c], cur_cnt[c])

        # Expand counts into the result list
        res = []
        for c, count in cnt.items():
            res.extend(c * count)   # 'l' * 2 -> "ll", extend adds each char

        return res