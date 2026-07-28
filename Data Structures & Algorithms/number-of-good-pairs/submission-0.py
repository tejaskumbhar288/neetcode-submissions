class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        my_map = {}
        result = 0

        for num in nums:
            my_map[num] = my_map.get(num, 0) + 1

        for key in my_map:
            count = my_map[key]
            result += ((count * (count-1))//2)
                

        return result