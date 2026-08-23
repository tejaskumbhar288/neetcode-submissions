from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        #most_common return top k elemets sorted by frequency
        result = []
        temp = count.most_common(k)
        print("temp = ", temp)
        
        for i in range(len(temp)):
            result.append(temp[i][0])

        return result