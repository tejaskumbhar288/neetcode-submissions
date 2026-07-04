class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort()
        largest = -1
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)-1, -1, -2):
            if i == 0 and nums[i] != nums[i+1]:
                return nums[0]

            elif nums[i] != nums[i-1]:
                largest = nums[i]
                break


        return largest
             
