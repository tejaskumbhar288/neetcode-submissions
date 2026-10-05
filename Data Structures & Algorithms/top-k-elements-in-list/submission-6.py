from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = Counter(nums).most_common(k)
        result = []
        
        for (key, value) in temp:
            result.append(key)

        return result
