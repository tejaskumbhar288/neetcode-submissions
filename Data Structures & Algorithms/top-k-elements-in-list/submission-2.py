from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_num = Counter(nums)
        temp = sorted_num.most_common(k)
        result = []

        for i in range(len(temp)):
            result.append(temp[i][0])

        return result