from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = Counter(nums)
        result = []

        top_k = temp.most_common(k)

        for key in top_k:
            result.append(key[0])

        return result