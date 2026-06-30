class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = []


        for num in nums:
            if num in my_dict:
                return True

            my_dict.append(num)

        return False