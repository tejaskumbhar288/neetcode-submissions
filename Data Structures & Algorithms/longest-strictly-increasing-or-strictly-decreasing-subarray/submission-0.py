class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        currLen = 1
        res = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                currLen = 1
            elif (i >= 2 and (nums[i-2] < nums[i-1]) != (nums[i-1] < nums[i])):
                #direction changed -> start new streak of length 2
                currLen = 2
            else:
                #continues monotonic
                currLen += 1

            res = max(res, currLen)

        return res