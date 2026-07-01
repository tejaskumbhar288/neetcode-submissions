class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}

        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1

        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        result = []

        for key in sorted_dict:
            if k <= 0:
                break
            else:
                result.append(key)
                k -= 1

        return result
            

        