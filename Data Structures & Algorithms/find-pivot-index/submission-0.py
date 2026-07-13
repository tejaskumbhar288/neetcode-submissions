class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum += num

        leftSum = 0
        for i in range(len(nums)):
            tempSum = sum - nums[i]
            if leftSum == (tempSum / 2):
                return i

            leftSum += nums[i]

        return -1