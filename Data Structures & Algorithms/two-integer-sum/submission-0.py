class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for index, value in enumerate(nums):
            number = target - value

            if number in my_dict:
                return [my_dict[number], index]

            my_dict[value] = index

            
        return []
