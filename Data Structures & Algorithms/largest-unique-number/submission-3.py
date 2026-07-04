class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        my_dict = {}
        largest = -1

        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1

        for key in my_dict:
            if my_dict[key] == 1 and key > largest:
                largest = key

        return largest             
