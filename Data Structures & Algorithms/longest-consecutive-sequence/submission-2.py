class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force solution
        nums.sort()
        if not nums:
            return 0
        maxLen = 1
        sum_len = 1
        print("nums = ", nums)
        if len(nums) == 1:
            return 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                sum_len += 1
            elif nums[i] != nums[i-1]:
                sum_len = 1

            maxLen = max(maxLen, sum_len)

        return maxLen